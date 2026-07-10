# DuplicateRestaurantError
# RestaurantAlreadyOpenError
# RestaurantAlreadyClosedError


class RestaurantError(Exception):
    pass

class RestaurantNotFoundError(RestaurantError):
    pass

class RestaurantAlreadyOpenError(RestaurantError):
    pass

class RestaurantAlreadyClosedError(RestaurantError):
    pass

class CategoryNotFoundError(RestaurantError):
    pass

class ItemNotFoundError(RestaurantError):
    pass

class DuplicateRestaurantError(RestaurantError):
    pass

class DuplicateCategoryError(RestaurantError):
    pass

class DuplicateItemError(RestaurantError):
    pass