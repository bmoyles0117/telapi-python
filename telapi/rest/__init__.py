from telapi.rest.resources.accounts import Account
from telapi.rest.resources.base import register_data_proxy
from telapi.rest.exceptions import AuthenticationError
from telapi.rest.exceptions import RestError

def authenticate(account_sid, auth_token, base_url = 'https://api.telapi.com/v1'):
    register_data_proxy(base_url, account_sid, auth_token)
    
    account = Account(sid=account_sid)
    
    return account.load()