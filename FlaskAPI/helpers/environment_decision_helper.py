import os 
from dotenv import load_dotenv

class EnvironmentDecisionHelper:
    
    def __init__(self):
        raise RuntimeError('Call _set_environment_flask_settings instead')

    @staticmethod
    def _set_environment_flask_settings():
        if os.environ.get("FLASK_ENV").lower() == "development":
            load_dotenv(".\development.env")
        elif os.environ.get("FLASK_ENV").lower() == "production":
            load_dotenv(".\production.env")
        else:
            raise Exception("No FLASK_ENV variable set")