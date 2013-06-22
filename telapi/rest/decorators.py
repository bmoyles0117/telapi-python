from telapi.rest.exceptions import AuthenticationError
from telapi.rest.exceptions import RestError

def transform_response(func):
    def inner(*args, **kwargs):
        response = func(*args, **kwargs)
        
        if response.status_code == 401:
            raise AuthenticationError('Invalid account credentials provided')
        
        if response.status_code == 404:
            raise RestError('Invalid REST API endpoint, perhaps an invalid SID', 404)
        
        json_response = response.json()
        
        if response.status_code != 200:
            raise RestError(json_response['message'], json_response['code'])
        
        return json_response
    
    return inner