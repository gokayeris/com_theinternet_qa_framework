"""Pruebas para el módulo de Basic Auth."""
import allure
from pages.basic_auth_page import BasicAuthPage

@allure.feature("Authentication")
def test_basic_auth_success(page):
    """Verifica el acceso exitoso con credenciales válidas."""
    auth_page = BasicAuthPage(page)

    with allure.step("Ingresar al sistema"):
        auth_page.login("admin", "admin")

    with allure.step("Validar mensaje de bienvenida"):
        assert "Basic Auth" in auth_page.get_success_message()
