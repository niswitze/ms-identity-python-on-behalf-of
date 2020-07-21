from flask import Flask, jsonify
from blueprints.subscriptions_bp import subscriptions
from helpers.authorization import AuthError
from dotenv import load_dotenv
import os

if os.environ.get("FLASK_ENV").lower() == "development":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UI.development_settings')
    load_dotenv(".\development.env")
elif os.environ.get("FLASK_ENV").lower() == "production":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UI.production_settings')
    load_dotenv(".\production.env")
else:
    raise Exception("No ENVIRONMENT variable set")

app = Flask(__name__)

app.register_blueprint(subscriptions)

#obtained from https://github.com/Azure-Samples/ms-identity-python-webapi-azurefunctions/blob/master/Function/secureFlaskApp/__init__.py
@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response