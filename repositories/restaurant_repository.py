from pathlib import Path
import os
import json

from models.restaurant import Restaurant

class RestaurantRepository:

    def __init__(self) -> None:
        self.directory = "data"
        self.file = os.path.join(self.directory,"Restaurant_Repository.json")

        

       



    def create_file(self):

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        

        if Path(self.file).exists():
            pass
        else:
            with open(self.file,"x") as fl:
                json.dump([],fl)

    def read_all(self):
        self.create_file()

        with open(self.file,"r") as file:
            data = json.load(file)
            return data
        

    def write_all(self,data: list[dict]):
    
        with open(self.file,"w") as file:
            json.dump(data,file,indent=4)
        print("Data write...")


    def save(self,restaurant):
        data = self.read_all()

        if self.find_by_id(restaurant.id):
            raise ValueError("Restaurant already exists.")

        data.append(restaurant.to_dict())

        self.write_all(data)

        print("data Saved...")

    def get_all(self):
        
        data = self.read_all()
        list_of_obj = [Restaurant.from_dict(restaurant) for restaurant in data]
        return list_of_obj

    def find_by_id(self,restaurantId:int):
        data = self.get_all()

        for restaurant in data:
            if restaurant.id == restaurantId:
                return restaurant
            
        return None

    def update(self,restaurant:Restaurant):
        
        data = self.get_all()

        for index,restaurant_obj in enumerate(data):
            if restaurant_obj.id == restaurant.id:
                data[index] = restaurant
                data_list = [obj.to_dict() for obj in data]
                self.write_all(data_list)
                return
        return None

        

    def delete(self,restaurantId:int):
        data = self.get_all()
        for index,restaurant in enumerate(data):
            if restaurant.id == restaurantId:
                data.pop(index)
                data_list = [obj.to_dict() for obj in data]
                self.write_all(data_list)
                print("Restaurant Deleted...")
                return
            
        print("Restaurant not found")

        











