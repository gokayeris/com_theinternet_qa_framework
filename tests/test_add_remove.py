"""Pruebas para el módulo de agregar/eliminar elementos."""

import allure
from pages.add_remove_page import AddRemovePage


@allure.feature("Add/Remove Elements")
def test_add_remove_elements(page):
    """Verifica que se puedan agregar y eliminar elementos dinámicamente."""
    add_remove = AddRemovePage(page)

    with allure.step("Navegar a la página de Add/Remove Elements"):
        add_remove.navigate()

    with allure.step("Agregar elementos y verificar"):
        add_remove.add_element()
        assert add_remove.is_delete_button_visible()

    with allure.step("Eliminar elemento y verificar"):
        add_remove.delete_element()
        assert not add_remove.is_delete_button_visible()
