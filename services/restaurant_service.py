from repositories.restaurant_repository import RestaurantRepository
from models.restaurant import Restaurant
from models.category import Category
from models.menu_item import MenuItem
from datetime import datetime



class RestaurantService:

    def __init__(self,restaurantRepository: RestaurantRepository):
        self.repository = restaurantRepository


    def create_restaurant(self,restaurant:Restaurant):
        self._validate_restaurant(restaurant)
        self._validate_time(restaurant.opening_time,restaurant.closing_time)
        self._check_restaurant_duplicates(restaurant)
        
        self.repository.save(restaurant)
        return restaurant
    

    def get_resaurant_by_id(self,restaurantId:int):
        rest = self.repository.find_by_id(restaurantId)
        if rest:
            return rest
        else:
            print("Restaurant Not found...")


    def get_all_restaurant(self):
        return self.repository.get_all()
    

    def update_restaurant(self,restaurant:Restaurant):
        self._validate_time(restaurant.opening_time,restaurant.closing_time)
        self._validate_restaurant(restaurant)
        if self.repository.update(restaurant):
            return restaurant
        raise ValueError("Restaurant not found...")


    def delete_restaurant(self,restaurantId:int):
        if self.repository.delete(restaurantId):
            return
        raise ValueError("Restaurant not found...")



    def open_restaurant(self,restaurantId:int):
        rest = self.repository.find_by_id(restaurantId)
        if rest:
            if not rest.is_active:
                rest.open_restaurant()
                self.repository.update(rest)       
        else:
            raise ValueError("Restaurant not found...")



    def close_restaurant(self,restaurantId:int):
        rest = self.repository.find_by_id(restaurantId)
        if rest:
            if rest.is_active:
                rest.close_restaurant()
                self.repository.update(rest)       
        else:
            raise ValueError("Restaurant not found...")
            


    def add_category(self,restaurantId:int,category:Category):
        rest = self.repository.find_by_id(restaurantId)
        if rest:
            self._validate_category(category)
            self._check_duplicate_category(rest,category)
            rest.add_category(category)
            self.repository.update(rest)
        else:
            raise ValueError("Restaurant not found...")



    def remove_category(self,restaurantId:int,categoryId:int):
        rest = self.repository.find_by_id(restaurantId)
        category = self._find_category(restaurantId,categoryId)
        
        if category:
            rest.remove_category(category)
            self.repository.update(rest)
        else:
            raise ValueError("Restaurant not found...")
                 


    def add_menu_item(self,restaurantId:int,categoryId:int,item:MenuItem):
        rest = self.repository.find_by_id(restaurantId)
        category = self._find_category(rest,categoryId)
        if category:
            self._validate_menu_item(item)
            self._check_menuItem_duplicate(category,item)
            category.add_item(item)
            self.repository.update(rest)
        else:
            raise ValueError("Restaurant not found...")
      
            
    def remove_menu_item(self,restaurantId:int,categoryId:int,itemId:int):
        rest = self.repository.find_by_id(restaurantId)
        category = self._find_category(rest,categoryId)
        item = self._find_menu_item(rest,category,itemId)
        if item:
            category.remove_item(itemId)
            self.repository.update(rest)
            return item
         


     

    def _validate_restaurant(self,restaurant:Restaurant):
        if not restaurant.name.strip():
            raise ValueError("Restaurant Name Required")
           
        if restaurant.owner is None:
            raise ValueError("Restaurant must have an Owner")
           
        if not restaurant.phone.strip():
            raise ValueError("Restaurant must have Phone Number")
           
        if not restaurant.email.strip():
            raise ValueError("Restaurant must have an Email")
        

    def _check_restaurant_duplicates(self,restaurant:Restaurant):

        if self.repository.find_by_id(restaurant.id):
            raise ValueError("Restaurant Id already exists")
        
        if self.repository.find_by_name(restaurant.name):
            raise ValueError("Restaurant Name already exists")
        
        if self.repository.find_by_phone(restaurant.phone):
            raise ValueError("Restaurant Phone already exists")
        
        if self.repository.find_by_email(restaurant.email):
            raise ValueError("Restaurant Email already exists")

    
    def _validate_time(self,opening_time:str,closing_time:str):
        try:
            opening = datetime.strptime(opening_time, "%H:%M")
            closing = datetime.strptime(closing_time, "%H:%M")
        except ValueError:
            raise ValueError("Time must be in HH:MM format and be valid.")
        
        if opening >= closing:
                raise ValueError("Opening time must be earlier than closing time.")
        
    def _find_category(self,restaurant:Restaurant,categoryId:int):
        if restaurant:
            for category in restaurant.categories:
                if category.id == categoryId:
                    return category
                
    def _find_menu_item(self,restaurant:Restaurant,category:Category,itemId:int):
        category = self._find_category(restaurant,category)
        if category:
            for item in category.menu_items:
                if item.id == itemId:
                    return item
        
    def _validate_category(self,category):
        if not category.name.strip():
            raise ValueError("Category Name Required")
        
    def _check_duplicate_category(self,restaurant:Restaurant,category:Category):
        for cate in restaurant.categories:
            if cate.id == category.id:
                raise ValueError("Category Id already exists")
            
            if cate.name == category.name:
                raise ValueError("Category Name already exists")
    
    def _validate_menu_item(self,item:MenuItem):
        if not item.name.strip():
            raise ValueError("Category Name Required")

        if item.price <= 0:
            raise ValueError("Price must be Greater than Zero")
        
        if item.preparation_time <= 0:
            raise ValueError("Price must be Greater than Zero")
        
    def _check_menuItem_duplicate(self,category:Category,item:MenuItem):
        for menu_ite in category.menu_items:
            if menu_ite.id == item.id:
                raise ValueError("Menu Item Id already exists")
            
            if menu_ite.name == item.name:
                raise ValueError("Menu Item Name already exists")




        




            
            
                



        

          
               

               



        