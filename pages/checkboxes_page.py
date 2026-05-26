"""Módulo para la página de Checkboxes."""
import allure
from playwright.sync_api import Page

class CheckboxesPage:
    """Clase para interactuar con la página de Checkboxes."""

    def __init__(self, page: Page):
        self.page = page
        self.checkboxes = "input[type='checkbox']"

    @allure.step("Navegar a la página de Checkboxes")
    def navigate(self):
        """Accede a la página de checkboxes."""
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")

    @allure.step("Cambiar estado del checkbox {index}")
    def toggle_checkbox(self, index):
        """Marca o desmarca el checkbox según su índice (0 o 1)."""
        self.page.locator(self.checkboxes).nth(index).click()

    @allure.step("Verificar si el checkbox {index} está marcado")
    def is_checked(self, index):
        """Retorna True si el checkbox está seleccionado."""
        return self.page.locator(self.checkboxes).nth(index).is_checked()
