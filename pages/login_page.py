"""Page Object que representa la página de inicio de sesión (Login)."""

from playwright.sync_api import Page
from config import Config
from utils.common_actions import CommonActions

class LoginPage:
    """Clase con los selectores y acciones para la página de Login."""

    def __init__(self, page: Page):
        self.page = page
        self.actions = CommonActions(page)

        # Construimos la URL usando tu Config
        self.url = f"{Config.BASE_URL_UI}/login"

        # Selectores en formato String para usar con tu CommonActions
        self.username_input_selector = "#username"
        self.password_input_selector = "#password"
        self.login_button_selector = "button[type='submit']"
        self.flash_message_selector = "#flash"

    def navigate(self):
        """Navega a la URL de inicio de sesión."""
        self.actions.navigate(self.url)

    def login(self, username: str, password: str):
        """Completa las credenciales y envía el formulario de login."""
        self.actions.fill(self.username_input_selector, username)
        self.actions.fill(self.password_input_selector, password)
        self.actions.click(self.login_button_selector)

    def get_flash_message_text(self) -> str:
        """Obtiene el texto del mensaje de alerta dinámico."""
        text = self.actions.get_element_text(self.flash_message_selector)
        return text.strip() if text else ""
