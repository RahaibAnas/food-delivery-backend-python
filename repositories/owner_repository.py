from pathlib import Path
import os
import json

from models.owner import Owner

class OwnerRepository:
    def __init__(self):
        self.dir = "data"
        self.file = os.path.join(self.dir,"Owner_Repository.json")

    def create_file(self):
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        if Path(self.file).exists():
            pass
        else:
            with open(self.file,"x") as file:
                json.dump([],file)

    def read_all(self):
        self.create_file()
        with open(self.file,"r") as file:
            data = json.load(file)
        return data
    
    def write_all(self,data:list[dict]):
        with open(self.file,"w") as file:
            json.dump(data,file,indent=4)
        print("Data Write...")

    def save(self,owner:Owner):
        data = self.read_all()
        data.append(owner.to_dict())
        self.write_all(data)

    def get_all(self):
        data = self.read_all()
        obj_list = [Owner.from_dict(owner) for owner in data]
        return obj_list
    
    def find_by_id(self,OwnerId:int):
        data = self.get_all()

        for owner in data:
            if owner.id == OwnerId:
                return owner
        return
            
    def find_by_email(self,OwnerEmail:str):
        data = self.get_all()
        for owner in data:
            if owner.email == OwnerEmail:
                return owner
        return

        
            
    def update(self,owner:Owner):
        data = self.get_all()
        for index,owner_obj in enumerate(data):
            if owner_obj.id == owner.id:
                data[index] = owner
                data = [owner.to_dict() for owner in data]
                self.write_all(data)
                print("Owner updated")
                return owner
        
         
    
    def delete(self,ownerId:int):
        data = self.get_all()
        for index,owner_obj in enumerate(data):
            if owner_obj.id == ownerId:
                data.pop(index)
                data = [owner.to_dict() for owner in data]
                self.write_all(data)
                print("Owner deleted")
                return ownerId
       
            


            
    
        

        



