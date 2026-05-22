import os
from dotenv import load_dotenv

# Cargamos las variables del archivo .env
load_dotenv()

class Config:
    # Leemos las variables. Si por alguna razón no existen, le ponemos un valor por defecto (fallback)
    BASE_URL_UI = os.getenv("BASE_URL_UI", "https://the-internet.herokuapp.com")
    BASE_URL_API = os.getenv("BASE_URL_API", "https://the-internet.herokuapp.com")
    
    # Acá podrías mapear otros ambientes si quisieras en el futuro
    # Ej: DEV_URL = "https://dev-the-internet.herokuapp.com"