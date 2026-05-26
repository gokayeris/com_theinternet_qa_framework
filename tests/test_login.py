"""Pruebas de automatización para el módulo de Login en The Internet."""
import allure
from pages.login_page import LoginPage


@allure.feature("Autenticación")  # Define la funcionalidad principal
@allure.story("Login exitoso")  # Define la historia de usuario
@allure.severity(allure.severity_level.CRITICAL)  # Define la importancia
def test_successful_login(page):
    """Verifica que un usuario con credenciales válidas pueda iniciar sesión."""
    login_page = LoginPage(page)

    with allure.step("Navegar a la página de login"):
        login_page.navigate()

    with allure.step("Ingresar credenciales válidas"):
        login_page.login("tomsmith", "SuperSecretPassword!")

    with allure.step("Validar mensaje de éxito"):
        flash_text = login_page.get_flash_message_text()
        expected = "You logged into a secure area!"
        assert expected in flash_text, f"Login fallido. Se obtuvo: '{flash_text}'"
