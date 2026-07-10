class ValidationError(Exception):
    pass

class InvalidNameError(ValidationError):
    pass

class InvalidOwnerError(ValidationError):
    pass

class InvalidPhoneError(ValidationError):
    pass

class InvalidEmailError(ValidationError):
    pass

class InvalidTimeError(ValidationError):
    pass

class InvalidCategoryError(ValidationError):
    pass

class InvalidMenuItemError(ValidationError):
    pass

class InvalidPasswordError(ValidationError):
    pass