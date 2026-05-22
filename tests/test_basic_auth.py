"""Configuración global de Pytest y ganchos de reporte (Hooks)."""

import allure
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):  # pylint: disable=unused-argument
    """Hook que captura pantallas y videos automáticamente en Allure si el test falla."""
    outcome = yield
    report = outcome.get_result()

    # Actuamos solo si el fallo ocurre en la fase de llamada (ejecución del test)
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            # 1. Adjuntar Captura de Pantalla a Allure
            try:
                screenshot_bytes = page.screenshot(full_page=True)
                allure.attach(
                    screenshot_bytes,
                    name="Screenshot_Fallo",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:  # pylint: disable=broad-exception-caught
                print(f"No se pudo tomar la captura para Allure: {e}")

            # 2. Adjuntar Video a Allure
            try:
                video_path = page.video.path() if page.video else None
                if video_path:
                    # Cerramos el contexto para asegurar que se guarde el archivo
                    page.context.close()
                    allure.attach.file(
                        video_path,
                        name="Video_Fallo",
                        attachment_type=allure.attachment_type.WEBM
                    )
            except Exception as e:  # pylint: disable=broad-exception-caught
                print(f"No se pudo adjuntar el video para Allure: {e}")
