class CustomerError(Exception):
    pass

class CustomerNotFoundError(CustomerError):
    pass

class CustomerDuplicateError(CustomerError):
    pass