from requests import Session, adapters
from urllib3.util.retry import Retry

class RequestsHelper:
    
    _backend_api_session = None

    def __init__(self):
        raise RuntimeError('Call _get_backend_api_session instead')

    @staticmethod
    def _get_backend_api_session(token_response):
        if RequestsHelper._backend_api_session is None:
            print('Creating new requests session')      
            session = Session()
            retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[ 500, 502, 503, 504 ])
            session.mount('https://', adapters.HTTPAdapter(max_retries=retries))
            session.mount('http://', adapters.HTTPAdapter(max_retries=retries))
            RequestsHelper._backend_api_session = session

        RequestsHelper._backend_api_session.headers= {'Authorization': token_response['token_type'] + ' ' + token_response['access_token']}
        return RequestsHelper._backend_api_session