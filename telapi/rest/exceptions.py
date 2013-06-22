class AuthenticationError(Exception):
    pass
    
class RestError(Exception):
    def __init__(self, message, error_code, *args):
        self.error_code = error_code
        
        super(RestError, self).__init__(message, *args)