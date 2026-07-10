from services.restaurant_service import RestaurantService
from models.restaurant import Restaurant
from models.category import Category
from models.menu_item import MenuItem

from exceptions import *

class RestaurantController:

    def __init__(self,service:RestaurantService):
        self.service =  service

    def create_restaurant(self,restaurant:Restaurant ):
        try:
            print("Service Runs Successfully")
            return self.service.create_restaurant(restaurant)
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
                print(f"Authentication Error: {e}")
        except AuthorizationError as e:
                print(f"Authorization Error: {e}")
        except RestaurantError as e:
                print(f"Restaurant Error: {e}")
        except Exception as e:
                print(f"Unexpected Error: {e}")

    # def get_restaurant_by_id(self,restaurantId:int):
    #     try:
    #         print("Service Runs Successfully")
    #         return self.service.get_resaurant_by_id(restaurantId)
    #     except ValueError as e:
    #         print(e)

    # def get_all_restaurant(self):
    #     try:
    #         print("Service Runs Successfully")
    #         return self.service.get_all_restaurant()
    #     except Exception as e:
    #         print(e)

    def update_restaurant(self,restaurant:Restaurant):
        try:
            print("Service Runs Successfully")
            return self.service.update_restaurant(restaurant)
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
                print(f"Authentication Error: {e}")
        except AuthorizationError as e:
                print(f"Authorization Error: {e}")
        except RestaurantError as e:
                print(f"Restaurant Error: {e}")
        except Exception as e:
                print(f"Unexpected Error: {e}")
            
    def delete_restaurant(self,restaurantId:int):
        try:
            self.service.delete_restaurant(restaurantId)
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
                print(f"Authentication Error: {e}")
        except AuthorizationError as e:
                print(f"Authorization Error: {e}")
        except RestaurantError as e:
                print(f"Restaurant Error: {e}")
        except Exception as e:
                print(f"Unexpected Error: {e}")
        else:
            print("Service Runs Successfully")

    def open_restaurant(self,restaurantId:int):
        try:
            self.service.open_restaurant(restaurantId)
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
                print(f"Authentication Error: {e}")
        except AuthorizationError as e:
                print(f"Authorization Error: {e}")
        except RestaurantError as e:
                print(f"Restaurant Error: {e}")
        except Exception as e:
                print(f"Unexpected Error: {e}")
        else:
            print("Service Runs Successfully")

    def close_restaurant(self,restaurantId:int):
        try:
            self.service.close_restaurant(restaurantId)
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
                print(f"Authentication Error: {e}")
        except AuthorizationError as e:
                print(f"Authorization Error: {e}")
        except RestaurantError as e:
                print(f"Restaurant Error: {e}")
        except Exception as e:
                print(f"Unexpected Error: {e}")
        else:
            print("Service Runs Successfully")

    def add_category(self,restaurantId:int,category:Category):
        try:
            self.service.add_category(restaurantId,category)
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
                print(f"Authentication Error: {e}")
        except AuthorizationError as e:
                print(f"Authorization Error: {e}")
        except RestaurantError as e:
                print(f"Restaurant Error: {e}")
        except Exception as e:
                print(f"Unexpected Error: {e}")
        else:
            print("Service Runs Successfully")

    def remove_category(self,restaurantId:int,categoryId:int):
        try:
            self.service.remove_category(restaurantId,categoryId)
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
                print(f"Authentication Error: {e}")
        except AuthorizationError as e:
                print(f"Authorization Error: {e}")
        except RestaurantError as e:
                print(f"Restaurant Error: {e}")
        except Exception as e:
                print(f"Unexpected Error: {e}")
        else:
            print("Service Runs Successfully")

    def add_menu_item(self,restaurantId: int, categoryId: int, item: MenuItem):
        try:
            self.service.add_menu_item(restaurantId,categoryId,item)
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
                print(f"Authentication Error: {e}")
        except AuthorizationError as e:
                print(f"Authorization Error: {e}")
        except RestaurantError as e:
                print(f"Restaurant Error: {e}")
        except Exception as e:
                print(f"Unexpected Error: {e}")
        else:
            print("Service Runs Successfully")

    def remove_menu_item(self,restaurantId: int, categoryId: int, itemId: int):
        try:
            self.service.remove_menu_item(restaurantId,categoryId,itemId)
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
                print(f"Authentication Error: {e}")
        except AuthorizationError as e:
                print(f"Authorization Error: {e}")
        except RestaurantError as e:
                print(f"Restaurant Error: {e}")
        except Exception as e:
                print(f"Unexpected Error: {e}")
        else:
            print("Service Runs Successfully")

        

            
            

    
