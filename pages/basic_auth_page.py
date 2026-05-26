"""Módulo para la página de Basic Auth."""
import allure
from playwright.sync_api import Page

class BasicAuthPage:
    """Clase para interactuar con la página de Basic Auth."""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/basic_auth"

    @allure.step("Realizar login con credenciales {user}/{password}")
    def login(self, user, password):
        """Autenticación básica inyectada en la URL."""
        auth_url = f"https://{user}:{password}@the-internet.herokuapp.com/basic_auth"
        self.page.goto(auth_url)

    @allure.step("Obtener mensaje de éxito")
    def get_success_message(self):
        """Retorna el texto de confirmación tras el login."""
        return self.page.locator("h3").text_content()
