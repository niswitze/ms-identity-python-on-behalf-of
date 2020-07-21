import os 
from dotenv import load_dotenv

class EnvironmentDecisionHelper:
    
    def __init__(self):
        raise RuntimeError('Call _set_environment_django_settings instead')

    @staticmethod
    def _set_environment_django_settings():
        if os.environ.get("ENVIRONMENT").lower() == "development":
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UI.development_settings')
            load_dotenv(".\development.env")
        elif os.environ.get("ENVIRONMENT").lower() == "production":
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UI.production_settings')
            load_dotenv(".\production.env")
        else:
            raise Exception("No ENVIRONMENT variable set")