from flask.views import MethodView
import requests

class ResoureGroupAPI(MethodView):

    def get(self):
        return {
            "resource_groupName1": "Test",
            "resource_groupName2": "Test2"
            }