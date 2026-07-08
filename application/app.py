from controllers.restaurant_controller import RestaurantController
from repositories.restaurant_repository import RestaurantRepository
from services.restaurant_service import RestaurantService
from models.restaurant import Restaurant

class FoodDeliveryApp:
    def __init__(self):
        restaurant_repository = RestaurantRepository()
        restaurant_services = RestaurantService(restaurant_repository)
        self.restaurant_controller = RestaurantController(restaurant_services)

    def start(self):
        
        pass
                    


        