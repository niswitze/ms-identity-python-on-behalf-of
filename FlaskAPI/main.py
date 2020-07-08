from flask import Flask
from .blueprints.resource_groups_bp import resource_groups

app = Flask(__name__)
app.register_blueprint(resource_groups)