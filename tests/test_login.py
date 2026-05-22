from pages.login_page import LoginPage

def test_successful_login(page, user_lifecycle):
    # 1. Instanciamos la página de Login pasándole el objeto 'page' de Playwright
    login_page = LoginPage(page)
    
    # 2. Navegamos a la pantalla de Login usando el método del POM
    login_page.navigate()
    
    # 3. Extraemos el usuario y contraseña dinámicos que creó nuestro fixture de API
    username = user_lifecycle["username"]
    password = user_lifecycle["password"]
    
    print(f"\n[TEST - UI] Intentando loguear con: {username}")
    
    # 4. Como 'The Internet' solo acepta "tomsmith" y "SuperSecretPassword!",
    # si usamos los datos aleatorios de la API va a fallar el login (lo cual es correcto).
    # Para ver el flujo completado con éxito por ahora, podés probar con los datos de arriba,
    # o mandar los dinámicos para validar el comportamiento del cartel de error.
    
    # Probemos con los dinámicos para ver cómo interactúa:
    login_page.login(username, password)
    
    # 5. Asertamos que la pantalla muestre que el usuario es inválido (porque no existe en este frontend estático)
    assert "is invalid" in login_page.flash_message.text_content()
    print("[TEST - UI] Validación de mensaje de error completada con éxito.")