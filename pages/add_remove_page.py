"""Page Object que representa la funcionalidad de agregar y quitar elementos."""

from playwright.sync_api import Page
from config import Config
from utils.common_actions import CommonActions

class AddRemovePage:
    """Clase con los selectores y lógica para interactuar con Add/Remove Elements."""

    def __init__(self, page: Page):
        self.page = page
        self.actions = CommonActions(page)

        # Construimos la URL usando tu Config
        self.url = f"{Config.BASE_URL_UI}/add_remove_elements/"

        # Selectores en formato String
        self.add_button_selector = "button >> text=Add Element"
        self.delete_buttons_selector = "button.added-manually"

    def navigate(self):
        """Navega a la página de agregar y quitar elementos."""
        self.actions.navigate(self.url)

    def click_add_element(self):
        """Hace clic en el botón para añadir un elemento nuevo."""
        self.actions.click(self.add_button_selector)

    def click_delete_element_at(self, index: int = 0):
        """Hace clic en un botón de eliminar específico según su índice."""
        locator = self.page.locator(self.delete_buttons_selector)
        if locator.count() > index:
            locator.nth(index).click()

    def get_delete_buttons_count(self) -> int:
        """Cuenta la cantidad de botones de eliminación visibles en la interfaz."""
        return self.page.locator(self.delete_buttons_selector).count()
