"""Page Object que maneja la autenticación básica (Basic Auth) por URL."""

from playwright.sync_api import Page
from config import Config
from utils.common_actions import CommonActions

class BasicAuthPage:
    """Clase para interactuar con la página protegida por Basic Auth."""

    def __init__(self, page: Page):
        self.page = page
        self.actions = CommonActions(page)

        # Limpiamos el prefijo 'https://' de la URL base para inyectar credenciales
        base_url_clean = Config.BASE_URL_UI.replace("https://", "")
        self.url = f"https://admin:admin@{base_url_clean}/basic_auth"

        # Selector en formato String
        self.success_message_selector = "p"

    def navigate(self):
        """Navega a la URL protegida inyectando las credenciales de acceso."""
        self.actions.navigate(self.url)

    def get_success_message_text(self) -> str:
        """Obtiene el texto de confirmación tras ingresar exitosamente."""
        text = self.actions.get_element_text(self.success_message_selector)
        return text.strip() if text else ""
