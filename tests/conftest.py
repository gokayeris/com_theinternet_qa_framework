import allure
import pytest
import uuid
from api.user_api import UserAPI
from config import Config

@pytest.fixture(scope="session")
def user_lifecycle(playwright):
    """Fixture que maneja el CRUD del usuario (Setup y Teardown) por cada test"""
    
    # 1. Creamos un contexto de API limpio de forma explícita usando el archivo .env
    api_request_context = playwright.request.new_context(base_url=Config.BASE_URL_API)
    
    # Se lo pasamos a tu cliente de API
    client = UserAPI(api_request_context)
    
    # 2. Generamos datos dinámicos únicos
    unique_id = str(uuid.uuid4())[:8]
    username = f"goky_qa_{unique_id}"
    password = f"SecurePass_{unique_id}!"
    
    # -------------------------------------------------------------------------
    # SETUP: CREATE (Llamada a la API antes del test)
    # -------------------------------------------------------------------------
    print(f"\n[SETUP - API] Creando usuario dinámico: {username}")
    # response = client.create_user(username, password)
    
    user_id = "fake_id_123"  # Simulamos el ID retornado
    
    # Retornamos el diccionario para que el test desempaquete los datos fácilmente
    yield {
        "client": client,
        "username": username,
        "password": password
    }
    
    # -------------------------------------------------------------------------
    # TEARDOWN: DELETE (Limpieza después del test)
    # -------------------------------------------------------------------------
    print(f"\n[TEARDOWN - API] Borrando usuario con ID: {user_id} para limpiar la DB...")
    # client.delete_user(user_id)
    
    # Destruimos el contexto de API al finalizar para no dejar fugas de memoria
    api_request_context.dispose()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook de Pytest que captura pantallas y videos automáticamente en Allure si el test falla"""
    outcome = yield
    report = outcome.get_result()
    
    # Actuamos solo si el fallo ocurre en la fase de llamada (ejecución del test)
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            # 1. Adjuntar Captura de Pantalla a Allure
            try:
                screenshot_bytes = page.screenshot(full_page=True)
                allure.attach(
                    screenshot_bytes, 
                    name="Screenshot_Fallo", 
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"No se pudo tomar la captura para Allure: {e}")
            
            # 2. Adjuntar Video a Allure
            try:
                video_path = page.video.path() if page.video else None
                if video_path:
                    # Cerramos el contexto para asegurar que Playwright guarde el archivo de video en disco
                    page.context.close() 
                    allure.attach.file(
                        video_path, 
                        name="Video_Fallo", 
                        attachment_type=allure.attachment_type.WEBM
                    )
            except Exception as e:
                print(f"No se pudo adjuntar el video para Allure: {e}")