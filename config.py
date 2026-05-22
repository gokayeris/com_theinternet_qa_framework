"""Configuración global del framework de automatización."""

import os
from dotenv import load_dotenv

# Cargamos las variables del archivo .env
load_dotenv()

class Config:
    """Clase que expone las variables de entorno para el proyecto."""
    # URL base para las pruebas de interfaz de usuario (UI)
    BASE_URL_UI = os.getenv("BASE_URL_UI", "https://the-internet.herokuapp.com")
