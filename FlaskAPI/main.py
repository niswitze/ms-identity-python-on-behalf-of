from flask import Flask, jsonify
from blueprints.subscriptions_bp import subscriptions
from helpers.authorization import AuthError
import os

if os.getenv("FLASK_ENV") == "development": 
    from dotenv import load_dotenv
    load_dotenv(".\local.env")

app = Flask(__name__)

app.register_blueprint(subscriptions)

#obtained from https://github.com/Azure-Samples/ms-identity-python-webapi-azurefunctions/blob/master/Function/secureFlaskApp/__init__.py
@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response