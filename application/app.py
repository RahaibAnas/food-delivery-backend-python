from controllers.restaurant_controller import RestaurantController
from repositories.restaurant_repository import RestaurantRepository
from services.restaurant_service import RestaurantService
from models.restaurant import Restaurant

from models.owner import Owner
from repositories.owner_repository import OwnerRepository
from services.auth_service import AuthService
from controllers.auth_controller import AuthController

class FoodDeliveryApp:
    def __init__(self):
        owner_repository = OwnerRepository()
        auth_service =  AuthService(owner_repository)
        self.auth_controller = AuthController(auth_service)

        restaurant_repository = RestaurantRepository()
        restaurant_services = RestaurantService(restaurant_repository,auth_service)
        self.restaurant_controller = RestaurantController(restaurant_services)

        

    def start(self):
        
        pass
                    


        