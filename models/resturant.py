from .category import Category
from .owner import Owner

class Resturant:
    def __init__(self,id:int,name:str,description:str,email:str,phone:str,address:str,openingTime: str,closingTime:str,isActive:bool,owner:Owner) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.email = email
        self.phone = phone
        self.address = address
        self.opening_time = openingTime
        self.closing_time = closingTime
        self.is_active = isActive
        self.owner : Owner = owner
        self.categories : list[Category] = []

    def add_category(self,category:Category):
        self.categories.append(category)
        print("Category Added...")

    def remove_category(self,name:str):
        for category in self.categories:
            if category.name.lower() == name.lower():
                self.categories.remove(category)
                print("Category Deleted...")
                return
            
    def find_category(self,name:str):
        for category in self.categories:
            if category.name.lower() == name.lower():
                return category
            
    def update_details(self,name:str | None = "",description:str | None = "",email:str | None = "",phone:str | None = "",address:str | None = "",openingTime: str | None = "",closingTime:str | None = ""):
        if name:
            self.name = name
            print("Name changed")

        if description:
            self.description = description
            print("description changed")

        if email:
            self.email = email
            print("email changed")

        if phone:
            self.phone = phone
            print("phone changed")

        if address:
            self.address = address
            print("address changed")

        if openingTime:
            self.opening_time = openingTime
            print("openingTime changed")

        if closingTime:
            self.closing_time = closingTime
            print("closingTime changed")

    def show_items(self):

        for category in self.categories:
            category.show_items()

    def is_open(self):
        print("Resturant Open" if self.is_active else "Resturant Closed")

    def open_resturant(self):
        if self.is_active:
            print("Resturant is Open")
        else:
            self.is_active = True
            print("Resturant is Open")


    def close_resturant(self):
        if not(self.is_active):
            print("Resturant is Close")
        else:
            self.is_active = False
            print("Resturant is Close")



    
    
        