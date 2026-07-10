
class AuthenticationError(Exception):
    pass

class loginRequiredError(AuthenticationError):
    pass

class InvalidCredentialsError(AuthenticationError):
    pass


class OwnerDuplicateError(AuthenticationError):
    pass 