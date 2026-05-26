"""Configuración global de Pytest y ganchos de reporte (Hooks)."""

import os
import allure
import pytest


@pytest.fixture(scope="session", autouse=True)
def create_environment_properties():
    """Crea el archivo de propiedades del entorno para el reporte de Allure."""
    allure_results_dir = "allure-results"

    if not os.path.exists(allure_results_dir):
        os.makedirs(allure_results_dir)

    properties_content = """Browser=Chromium
BaseURL=https://the-internet.herokuapp.com
Environment=QA
OS=Windows 11
"""

    with open(
        os.path.join(allure_results_dir, "environment.properties"),
        "w",
        encoding="utf-8",
    ) as file:
        file.write(properties_content)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):  # pylint: disable=unused-argument
    """Hook que captura pantallas y videos automáticamente en Allure si el test falla."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            try:
                screenshot_bytes = page.screenshot(full_page=True)
                allure.attach(
                    screenshot_bytes,
                    name="Screenshot_Fallo",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception as e:  # pylint: disable=broad-exception-caught
                print(f"No se pudo tomar la captura para Allure: {e}")

            try:
                video_path = page.video.path() if page.video else None
                if video_path:
                    page.context.close()
                    allure.attach.file(
                        video_path,
                        name="Video_Fallo",
                        attachment_type=allure.attachment_type.WEBM,
                    )
            except Exception as e:  # pylint: disable=broad-exception-caught
                print(f"No se pudo adjuntar el video para Allure: {e}")
