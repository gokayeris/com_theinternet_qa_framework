"""Módulo para la página de Add/Remove Elements."""

import allure
from playwright.sync_api import Page


class AddRemovePage:
    """Clase para interactuar con la página de Add/Remove."""

    def __init__(self, page: Page):
        self.page = page
        self.add_button = "text=Add Element"
        self.delete_button = ".added-manually"

    @allure.step("Agregar un elemento")
    def add_element(self):
        """Hace clic en el botón para agregar un nuevo elemento."""
        self.page.click(self.add_button)

    @allure.step("Eliminar un elemento")
    def delete_element(self):
        """Hace clic en el botón para eliminar un elemento."""
        self.page.click(self.delete_button)

    @allure.step("Verificar si el botón de eliminar es visible")
    def is_delete_button_visible(self):
        """Retorna True si el botón de eliminar está visible, False en caso contrario."""
        return self.page.is_visible(self.delete_button)

    @allure.step("Navegar a la página")
    def navigate(self):
        """Navega a la URL de la página de Add/Remove Elements."""
        self.page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
