import json
from pathlib import Path
import os

from models.customer import Customer


class CustomerRepository:
    def __init__(self):
        self.dir = "data"
        self.file = os.path.join(self.dir,"customer_repository.json")

    def create_file(self):
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

        if not Path(self.file).exists():
            with open(self.file,"x") as file:
                json.dump([],file)

    def read_all(self):
        self.create_file()
        with open(self.file,"r") as file:
            data = json.load(file)
        return data

    def write_all(self,data: list[dict]):
        with open(self.file,"w") as file:
            json.dump(data,file,indent=4)
        print("data Write")

    def save(self,customer:Customer):
        data = self.read_all()
        data.append(customer.to_dict())
        self.write_all(data)
        print("Data Save")

    def get_all(self):
        data = self.read_all()
        obj_list = [Customer.from_dict(customer) for customer in data]
        return obj_list
    
    def find_by_id(self,customerId:int):
        data = self.get_all()
        for customer in data:
            if customer.id == customerId:
                return customer
            
    def find_by_email(self,customerEmail:str):
        data = self.get_all()
        for customer in data:
            if customer.email == customerEmail:
                return customer
    def find_by_phone(self,customerPhone:str):
        data = self.get_all()
        for customer in data:
            if customer.phone_number == customerPhone:
                return customer
            
    def find_by_name(self,customerName:str):
        data = self.get_all()
        for customer in data:
            if customer.name == customerName:
                return customer
    
    def update(self,customer:Customer):
        data = self.get_all()
        for index,cust in enumerate(data):
            if cust.id == customer.id:
                data[index] = customer
                data = [customer.to_dict() for customer in data]
                self.write_all(data)
                print("Data Updated")
                return customer

    def delete(self,customerId):
        data = self.get_all()
        for index,cust in enumerate(data):
            if cust.id == customerId:
                data.pop(index)
                data = [customer.to_dict() for customer in data]
                self.write_all(data)
                print("Data Deleted")
                return customerId
            



    
        