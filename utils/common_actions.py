"""Acciones comunes y wrappers interactivos sobre los métodos nativos de Playwright."""

from playwright.sync_api import Page

class CommonActions:
    """Clase que encapsula interacciones repetitivas de la interfaz de usuario."""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Navega a una URL específica."""
        self.page.goto(url)

    def click(self, selector: str):
        """Espera automáticamente y hace clic en un elemento."""
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str):
        """Limpia el campo y escribe texto en un elemento de entrada."""
        self.page.locator(selector).fill(text)

    def is_visible(self, selector: str) -> bool:
        """Verifica si un elemento es visible en la pantalla."""
        try:
            return self.page.locator(selector).is_visible()
        except Exception:  # pylint: disable=broad-exception-caught
            return False

    def wait_for_hidden(self, selector: str, timeout: float = 5000):
        """Espera explícitamente a que un elemento desaparezca de la interfaz."""
        self.page.locator(selector).wait_for(state="hidden", timeout=timeout)

    def get_element_text(self, selector: str) -> str:
        """Obtiene el contenido de texto de un elemento."""
        text = self.page.locator(selector).text_content()
        return text if text else ""
