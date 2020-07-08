import msal, os


class AuthenticationHelper:
    
    _confidential_client = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @staticmethod
    def get_confidential_client():
        if AuthenticationHelper._confidential_client is None:
            print('Creating new confidential client')
            #This example only uses the default memory token cache and should not be used for production
            AuthenticationHelper._confidential_client = msal.ConfidentialClientApplication(
                os.environ.get("CLIENT_ID"),
                authority=os.environ.get("AUTHORITY"),
                client_credential=os.environ.get("CLIENT_SECRET"))
        return AuthenticationHelper._confidential_client