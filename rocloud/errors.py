from typing import Dict

class HTTPException(Exception):
    ERRORS: Dict[str, str] = {
        'INVALID_ARGUMENT': 'You have passed an invalid argument.',
        'INSUFFICIENT_SCOPE': 'The request made requires higher privileges than provided by the access token.',
        'PERMISSION_DENIED': 'You do not have sufficient scopes to perform this request.',
        'NOT_FOUND': 'Cannot find resources provided.',
        'ABORTED': 'Operation caused conflict, request was aborted.',
        'RESOURCE_EXHAUSTED': 'Too many requests have been sent.',
        'CANCELLED': 'System terminated request, caused by client timeout.',
        'INTERNAL': 'Server error caused, typically a server bug.',
        'NOT_IMPLEMENTED': 'The server has not implemented this API Method.',
        'UNAVAILABLE': 'The request for this service is currently unavailable. The common cause for this is because of server downtime.',
    }
    def __init__(self, error):
        super().__init__(self.ERRORS.get(error, 'Unknown error caused.'))
