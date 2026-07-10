from models.category import Category
from models.menu_item import MenuItem
from models.owner import Owner
from models.restaurant import Restaurant

from repositories.restaurant_repository import RestaurantRepository
from repositories.owner_repository import OwnerRepository

from services.restaurant_service import RestaurantService
from services.auth_service import AuthService

from controllers.restaurant_controller import RestaurantController
from controllers.auth_controller import AuthController

from application.app import FoodDeliveryApp

from exceptions import *
 

# Owner

owner = Owner(1,"Rahaib","03218856814","rahaib@gmail.com","qwerty")

# Pizzas

menu_item_01 = MenuItem(1,"cheez pizza","this is cheez pizza",10.9,True,20)
menu_item_02 = MenuItem(2,"Margherita pizza","this is Margherita pizza",10.9,True,20)
menu_item_03 = MenuItem(3,"Pepperoni Pizza","this is Pepperoni Pizza",15.9,True,20)
menu_item_04 = MenuItem(4,"BBQ Chicken Pizza","this is BBQ Chicken Pizza",17.9,True,20)

category1 = Category(1,"Pizza")

# category1.add_item(menu_item_01,menu_item_02,menu_item_03,menu_item_04)


# Burgers

menu_item_11 = MenuItem(1,"Classic Beef Burger","this is Classic Beef Burger",5.9,True,10)
menu_item_12 = MenuItem(2,"Zinger Burger","this is Zinger Burger",3.9,True,10)
menu_item_13 = MenuItem(3,"Chicken Cheese Burger","this is Chicken Cheese Burger",12.9,True,10)
menu_item_14 = MenuItem(4,"Double Patty Burger","this is Double Patty Burger",8.9,True,10)

category2 = Category(2,"Burgers")

# category2.add_item(menu_item_11,menu_item_12,menu_item_13,menu_item_14)

# Fries

menu_item_21 = MenuItem(1,"Regular Fries","this is Regular Fries",2.9,True,15)
menu_item_22 = MenuItem(2,"Loaded Fries","this is Loaded Fries",1.9,True,15)
menu_item_23 = MenuItem(3,"Cheese Fries","this is Cheese Fries",3.9,True,15)
menu_item_24 = MenuItem(4,"Masala Fries","this is Masala Fries",4.9,True,15)

category3 = Category(3,"Fries")

# category3.add_item(menu_item_21,menu_item_22,menu_item_23,menu_item_24)

# Sandwiches

menu_item_31 = MenuItem(1,"Club Sandwich","this is Club Sandwich",20.9,True,20)
menu_item_32 = MenuItem(2,"Grilled Chicken Sandwich","this is Grilled Chicken Sandwich",20.9,True,20)
menu_item_33 = MenuItem(3,"Crispy Chicken Sandwich","this is Crispy Chicken Sandwich",20.9,True,20)
menu_item_34 = MenuItem(4,"Tuna Sandwich","this is Tuna Sandwich",20.9,True,20)

category4 = Category(4,"Sandwiches")

# category4.add_item(menu_item_31,menu_item_32,menu_item_33,menu_item_34)


# owners

owner1 = Owner(1,"Rahaib","03001234567","rahaib@gmail.com","Qwerty@1234")
owner2 = Owner(2,"Meer","03218856814","meer@gmail.com","Qwerty@1234")


#  Restaurant

restaurant1 = Restaurant(1,"BFC","this is BFC","bfc@gmail.com","03221234567","SHEIKHUPURA","12:00","22:10",False,owner1)

# restaurant1.add_category(category1)
# restaurant1.add_category(category2)
# restaurant1.add_category(category3)

# restaurant1.add_category(category4)

restaurant2 = Restaurant(2,"KFC","this is KFC","kfc@gmail.com","03001234567","lahore","10:00","22:10",True,owner2)

# restaurant2.add_category(category1)
# restaurant2.add_category(category2)
# restaurant2.add_category(category3)

# restaurant2.add_category(category4)










app = FoodDeliveryApp()

controller = app.restaurant_controller
auth = app.auth_controller

# auth.login("rahaib@gmail.com","Rah@1234A")

# print(auth.current_user())

auth.change_password("Qwerty@1234","Rah@1234A")

















