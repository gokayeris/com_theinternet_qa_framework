from playwright.sync_api import Page
from config import Config  # <- Importamos la configuración

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Usamos la variable del .env para armar la URL de la interfaz
        self.url = f"{Config.BASE_URL_UI}/login"
        
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.flash_message = page.locator("#flash")

    def navigate(self):
        """Navega directamente a la URL de login"""
        self.page.goto(self.url)

    def login(self, username, password):
        """Acción combinada: Llena el formulario y hace click en ingresar"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()