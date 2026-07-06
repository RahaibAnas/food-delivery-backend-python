from .category import Category
from .owner import Owner

class Restaurant:
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
        print("Restaurant Open" if self.is_active else "Restaurant Closed")

    def open_restaurant(self):
        if self.is_active:
            print("Restaurant is Open")
        else:
            self.is_active = True
            print("Restaurant is Open")


    def close_restaurant(self):
        if not(self.is_active):
            print("Restaurant is Close")
        else:
            self.is_active = False
            print("Restaurant is Close")

    def to_dict(self):
        return{
            "Id": self.id,
            "Name": self.name,
            "Description": self.description,
            "Email": self.email,
            "Phone": self.phone,
            "Address": self.address,
            "Opening time": self.opening_time,
            "Closing time": self.closing_time,
            "Is active": self.is_active,
            "Owner": self.owner.to_dict(),
            "Categories": [category.to_dict() for category in self.categories]
        }
    
    @classmethod
    def from_dict(cls,data):
        restaurant =  cls(
            data["Id"],
            data["Name"],
            data["Description"],
            data["Email"],
            data["Phone"],
            data["Address"],
            data["Opening time"],
            data["Closing time"],
            data["Is active"],
            Owner.from_dict(data["Owner"])
        )

        restaurant.categories = [Category.from_dict(category) for category in data["Categories"]]

        return restaurant


    
    
        