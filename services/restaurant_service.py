from repositories.restaurant_repository import RestaurantRepository
from services.auth_service import AuthService
from models.restaurant import Restaurant
from models.category import Category
from models.menu_item import MenuItem
from models.owner import Owner
from datetime import datetime

from exceptions import *



class RestaurantService:

    def __init__(self,restaurantRepository: RestaurantRepository,authServices:AuthService):
        self.restaurant_repository = restaurantRepository
        self.auth_service =  authServices


    def create_restaurant(self,restaurant:Restaurant):
        self._login_required()
        restaurant.owner = self.auth_service.get_current_user()
        self._owner_check(restaurant)
        self._validate_restaurant(restaurant)
        self._validate_time(restaurant.opening_time,restaurant.closing_time)
        self._check_restaurant_duplicates(restaurant)
        
        self.restaurant_repository.save(restaurant)
        return restaurant
    

    def get_resaurant_by_id(self,restaurantId:int):
        rest = self.restaurant_repository.find_by_id(restaurantId)
        if rest:
            return rest
        raise RestaurantNotFoundError("Restaurant not found")


    def get_all_restaurant(self):
        return self.restaurant_repository.get_all()
    

    def update_restaurant(self,restaurant:Restaurant):
        self._login_required()
        self._owner_check(restaurant)
        self._validate_time(restaurant.opening_time,restaurant.closing_time)
        self._validate_restaurant(restaurant)
        self.restaurant_repository.update(restaurant)
        return restaurant


    def delete_restaurant(self,restaurantId:int):
        rest = self.restaurant_repository.find_by_id(restaurantId)
        if rest:
            self._login_required()
            self._owner_check(rest)
            if self.restaurant_repository.delete(restaurantId):
                return
        raise RestaurantNotFoundError("Restaurant not found...")
        



    def open_restaurant(self,restaurantId:int):
        rest = self.restaurant_repository.find_by_id(restaurantId)
        if rest:
            self._login_required()
            self._owner_check(rest)
            if not rest.is_active:
                rest.open_restaurant()
                self.restaurant_repository.update(rest) 
                return
            raise RestaurantAlreadyOpenError("Restaurant already Opened")      
        return rest



    def close_restaurant(self,restaurantId:int):
        rest = self.restaurant_repository.find_by_id(restaurantId)
        if rest:
            self._login_required()
            self._owner_check(rest)
            if rest.is_active:
                rest.close_restaurant()
                self.restaurant_repository.update(rest) 
                return 
            raise RestaurantAlreadyClosedError("Restaurant already Closed")      
                 
        raise RestaurantNotFoundError("Restaurant not found...")
            


    def add_category(self,restaurantId:int,category:Category):
        rest = self.restaurant_repository.find_by_id(restaurantId)
        if rest:
            self._login_required()
            self._owner_check(rest)
            self._validate_category(category)
            self._check_duplicate_category(rest,category)
            rest.add_category(category)
            self.restaurant_repository.update(rest)
            return
        raise RestaurantNotFoundError("Restaurant not found...")



    def remove_category(self,restaurantId:int,categoryId:int):
        rest = self.restaurant_repository.find_by_id(restaurantId)     
        if rest:
            self._login_required()
            self._owner_check(rest)
            rest.remove_category(categoryId)
            self.restaurant_repository.update(rest)
            return
        raise RestaurantNotFoundError("Restaurant not found...")
                 


    def add_menu_item(self,restaurantId:int,categoryId:int,item:MenuItem):
        rest = self.restaurant_repository.find_by_id(restaurantId)
        if rest:
            self._login_required()
            self._owner_check(rest)
            category = rest.find_category(categoryId)
            if category:
                self._validate_menu_item(item)
                self._check_menuItem_duplicate(category,item)
                category.add_item(item)
                self.restaurant_repository.update(rest)
                return item
            raise CategoryNotFoundError("Category not found")
        raise RestaurantNotFoundError("Restaurant not found...")

        
      
            
    def remove_menu_item(self,restaurantId:int,categoryId:int,itemId:int):
        rest = self.restaurant_repository.find_by_id(restaurantId)
        if rest:
            self._login_required()
            self._owner_check(rest)
            category = rest.find_category(categoryId)
            if category is None:
                raise CategoryNotFoundError("Category not found.")
            item = category.find_item(itemId)
            if item:
                category.remove_item(itemId)
                self.restaurant_repository.update(rest)
                return item
            raise ItemNotFoundError("Item not found")
        raise RestaurantNotFoundError("Restaurant not found...")
    
          
         


     

    def _validate_restaurant(self,restaurant:Restaurant):
        if not restaurant.name.strip():
            raise InvalidNameError("Restaurant Name Required")
           
        if restaurant.owner is None:
            raise InvalidOwnerError("Restaurant must have an Owner")
           
        if not restaurant.phone.strip():
            raise InvalidPhoneError("Restaurant must have Phone Number")
           
        if not restaurant.email.strip():
            raise InvalidEmailError("Restaurant must have an Email")
        
        return restaurant
        

    def _check_restaurant_duplicates(self,restaurant:Restaurant):

        if self.restaurant_repository.find_by_id(restaurant.id):
            raise DuplicateRestaurantError("Restaurant Id already exists")
        
        if self.restaurant_repository.find_by_name(restaurant.name):
            raise DuplicateRestaurantError("Restaurant Name already exists")
        
        if self.restaurant_repository.find_by_phone(restaurant.phone):
            raise DuplicateRestaurantError("Restaurant Phone already exists")
        
        if self.restaurant_repository.find_by_email(restaurant.email):
            raise DuplicateRestaurantError("Restaurant Email already exists")
        
        return restaurant

    
    def _validate_time(self,opening_time:str,closing_time:str):
        try:
            opening = datetime.strptime(opening_time, "%H:%M")
            closing = datetime.strptime(closing_time, "%H:%M")
        except InvalidTimeError:
            raise InvalidTimeError("Time must be in HH:MM format and be valid.")
        
        if opening >= closing:
                raise InvalidTimeError("Opening time must be earlier than closing time.")
        
        return True
        
    
        
    def _validate_category(self,category):
        if not category.name.strip():
            raise InvalidCategoryError("Category Name Required")
        
    def _check_duplicate_category(self,restaurant:Restaurant,category:Category):
        for cate in restaurant.categories:
            if cate.id == category.id:
                raise DuplicateCategoryError("Category Id already exists")
            
            if cate.name == category.name:
                raise DuplicateCategoryError("Category Name already exists")
    
    def _validate_menu_item(self,item:MenuItem):
        if not item.name.strip():
            raise InvalidMenuItemError("Category Name Required")

        if item.price <= 0:
            raise InvalidMenuItemError("Price must be Greater than Zero")
        
        if item.preparation_time <= 0:
            raise InvalidMenuItemError("Price must be Greater than Zero")
        
    def _check_menuItem_duplicate(self,category:Category,item:MenuItem):
        for menu_ite in category.menu_items:
            if menu_ite.id == item.id:
                raise DuplicateItemError("Menu Item Id already exists")
            
            if menu_ite.name == item.name:
                raise DuplicateItemError("Menu Item Name already exists")
            
            
    def _login_required(self):
        login = self.auth_service.is_logged_in()
        if not login:
            raise loginRequiredError("Login Required.")
        return login

    def _owner_check(self,restaurant:Restaurant):
        current = self.auth_service.get_current_user()
        stored_rest = self.restaurant_repository.find_by_id(restaurant.id)
        if stored_rest:
            if stored_rest.owner.id !=current.id:
                raise PermissionDeinedError("Permission Denied.")
        else:
            return
        


    
        
        




        




            
            
                



        

          
               

               



        