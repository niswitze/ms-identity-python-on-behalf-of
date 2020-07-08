from flask import Blueprint
from views.resource_groups_view import ResoureGroupAPI

resource_groups = Blueprint('resource_groups', __name__)


resource_groups.add_url_rule('/resoureGroups', view_func=ResoureGroupAPI.as_view("resource_groups_view"), methods=['GET'])
