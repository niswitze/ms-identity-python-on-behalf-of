from flask.views import MethodView
from flask import request
from helpers.authorization import AuthError
from helpers.authorization import requires_jwt_authorization
from helpers.msal_helper import AuthenticationHelper
import requests as req, os


class SubscriptionsAPI(MethodView):

    decorators = [requires_jwt_authorization]

    def get(self):

        current_access_token = request.headers.get("Authorization", None)

        if current_access_token is None:
            raise AuthError({"code": "invalid_header","description":"Unable to parse authorization"" token."}, 401)

        arm_resource_access_token = AuthenticationHelper.get_confidential_client().acquire_token_on_behalf_of(
            user_assertion=current_access_token.split(' ')[1],
            scopes=[os.environ.get("SCOPE")]
        )

        if "error" in arm_resource_access_token:
            raise AuthError({"code": arm_resource_access_token.get("error"),"description":""+arm_resource_access_token.get("error_description")+""}, 404)

        headers = {'Authorization': arm_resource_access_token['token_type'] + ' ' + arm_resource_access_token['access_token']}

        subscriptions_list = req.get(os.environ.get("AZURE_MANAGEMENT_SUBSCRIPTIONS_URI"), headers=headers).json()

        return subscriptions_list