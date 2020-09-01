from django.views import View
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from Helpers.msal_helper import AuthenticationHelper
import os, uuid



# Create your views here.
class LoginView(View):

    def get(self, request):

        request.session['auth_state'] = str(uuid.uuid4())

        sign_in_url = AuthenticationHelper.get_confidential_client().get_authorization_request_url(
            scopes=[os.environ.get("SCOPE")],
            state=request.session['auth_state'],
            redirect_uri=os.environ.get("REDIRECT_URI")
        )

        return HttpResponseRedirect(sign_in_url)


class LogOutView(View):

    def get(self, request):

        request.session.flush()

        logout(request)

        accounts = AuthenticationHelper.get_confidential_client().get_accounts(username=request.user.username)

        if len(accounts) != 0:
            AuthenticationHelper.get_confidential_client().remove_account(account=accounts[0])
            
        logout_url = os.environ.get("AUTHORITY") + os.environ.get("LOGOUT_URL") + os.environ.get("POST_LOGOUT_REDIRECT_URI")

        return HttpResponseRedirect(logout_url)


class CallbackView(View):

    def get(self, request):
        expected_state = request.session['auth_state']

        if request.GET.get('state') != expected_state:
            return HttpResponse("State obtained from callback was not the same as state passed in from the authorization url",status=404)

        if "error" in request.GET: 
            return HttpResponse("An Error Occured:" + request.GET.get("error") + " " +  request.GET.get("error_description"), status=403)

        token_response = AuthenticationHelper.get_confidential_client().acquire_token_by_authorization_code(
            code=request.GET.get('code'),
            scopes=[os.environ.get("SCOPE")],
            redirect_uri=os.environ.get("REDIRECT_URI")
        )

        if "error" in token_response:
            return HttpResponse("An Error Occured:" + token_response.get("error") + " " +  token_response.get("error_description"), status=404)

        try:
            current_session_user = User.objects.get(username=token_response['id_token_claims']['preferred_username'])
        except ObjectDoesNotExist as error:
            current_session_user = User.objects.create_user(username=token_response['id_token_claims']['preferred_username'], email=token_response['id_token_claims']['preferred_username'], password=str(uuid.uuid4()))

        login(request, current_session_user)

        return HttpResponseRedirect(reverse("azure_management_home"))


