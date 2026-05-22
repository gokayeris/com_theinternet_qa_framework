"""Pruebas funcionales de extremo a extremo para el módulo de Login."""

from pages.login_page import LoginPage

def test_successful_login(page):
    """Verifica que un usuario con credenciales válidas pueda iniciar sesión."""
    # 1. Inicializamos la página de Login
    login_page = LoginPage(page)

    # 2. Navegamos a la URL de login
    login_page.navigate()

    # 3. Ejecutamos la acción de login con credenciales válidas
    login_page.login("tomsmith", "SuperSecretPassword!")

    # 4. Obtenemos el texto del mensaje de alerta (flash message)
    flash_text = login_page.get_flash_message_text()

    # 5. Validamos que el login haya sido exitoso chequeando el texto esperado
    expected = "You logged into a secure area!"
    msg_err = f"Login fallido o mensaje incorrecto. Se obtuvo: '{flash_text}'"
    assert expected in flash_text, msg_err
