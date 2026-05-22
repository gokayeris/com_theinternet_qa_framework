from playwright.sync_api import APIRequestContext

class UserAPI:
    def __init__(self, request_context: APIRequestContext):
        self.request = request_context
        self.base_url = "https://the-internet.herokuapp.com"

    def create_user(self, username, password):
        """CREATE: Registra un nuevo usuario en el sistema"""
        payload = {
            "username": username,
            "password": password
        }
        # Acá simularíamos el endpoint real de la empresa, ej: /api/authenticate o /api/users
        response = self.request.post(f"{self.base_url}/authenticate", data=payload)
        return response

    def get_user_details(self, user_id):
        """READ: Obtiene los datos del usuario actual"""
        response = self.request.get(f"{self.base_url}/api/users/{user_id}")
        return response

    def update_user(self, user_id, new_data):
        """UPDATE: Modifica datos del usuario (contraseña, perfil, etc.)"""
        response = self.request.put(f"{self.base_url}/api/users/{user_id}", data=new_data)
        return response

    def delete_user(self, user_id):
        """DELETE: Borra el usuario para dejar la base de datos limpia"""
        response = self.request.delete(f"{self.base_url}/api/users/{user_id}")
        return response