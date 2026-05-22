"""Pruebas funcionales de extremo a extremo para la adición y eliminación de elementos."""

from pages.add_remove_page import AddRemovePage

def test_add_remove_elements(page):
    """Valida el flujo dinámico de agregar botones y luego borrarlos de la UI."""
    # 1. Inicializamos la página con el objeto del navegador
    add_remove_page = AddRemovePage(page)

    # 2. Navegamos a la URL correspondiente
    add_remove_page.navigate()

    # 3. Validamos que inicialmente no haya botones de "Delete"
    msg_init = "Debería haber 0 botones de Delete al iniciar"
    assert add_remove_page.get_delete_buttons_count() == 0, msg_init

    # 4. Hacemos clic en agregar elemento
    add_remove_page.click_add_element()

    # 5. Validamos que ahora aparezca un botón de "Delete"
    msg_add = "Debería haber 1 botón de Delete después de agregarlo"
    assert add_remove_page.get_delete_buttons_count() == 1, msg_add

    # 6. Borramos el elemento agregado
    add_remove_page.click_delete_element_at(0)

    # 7. Validamos que vuelva a quedar en 0
    msg_del = "Debería haber 0 botones de Delete después de eliminarlo"
    assert add_remove_page.get_delete_buttons_count() == 0, msg_del
