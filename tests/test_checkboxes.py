"""Pruebas para el módulo de Checkboxes."""

import allure
from pages.checkboxes_page import CheckboxesPage


@allure.feature("Checkboxes")
def test_checkbox_selection(page):
    """Verifica que los checkboxes se pueden marcar y desmarcar."""
    cb_page = CheckboxesPage(page)

    with allure.step("Preparar estado inicial"):
        cb_page.navigate()

    with allure.step("Marcar primer checkbox"):
        if not cb_page.is_checked(0):
            cb_page.toggle_checkbox(0)
        assert cb_page.is_checked(0)

    with allure.step("Desmarcar segundo checkbox"):
        if cb_page.is_checked(1):
            cb_page.toggle_checkbox(1)
        assert not cb_page.is_checked(1)
