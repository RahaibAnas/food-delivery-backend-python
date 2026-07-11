from repositories.restaurant_repository import RestaurantRepository
from services.restaurant_service import RestaurantService
from controllers.restaurant_controller import RestaurantController

from repositories.owner_repository import OwnerRepository
from services.auth_service import AuthService
from controllers.auth_controller import AuthController

from repositories.customer_repository import CustomerRepository
from services.customer_service import CustomerService
from controllers.customer_controller import CustomerController

class FoodDeliveryApp:
    def __init__(self):
        owner_repository = OwnerRepository()
        auth_service =  AuthService(owner_repository)
        self.auth_controller = AuthController(auth_service)

        restaurant_repository = RestaurantRepository()
        restaurant_services = RestaurantService(restaurant_repository,auth_service)
        self.restaurant_controller = RestaurantController(restaurant_services)

        customer_repository = CustomerRepository()
        customer_service = CustomerService(customer_repository)
        self.customer_controller = CustomerController(customer_service)

 

        