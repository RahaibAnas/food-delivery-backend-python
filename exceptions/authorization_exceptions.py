class AuthorizationError(Exception):
    pass

class PermissionDeinedError(AuthorizationError):
    pass