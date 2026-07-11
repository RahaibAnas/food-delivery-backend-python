from services.customer_service import CustomerService
from models.customer import Customer

from exceptions import *

class CustomerController:
    def __init__(self,customerService:CustomerService):
        self.service =  customerService

    def register(self,customer:Customer):
        try:
            return self.service.register(customer)
        except CustomerError as e:
            print(f"Customer Error: {e}")
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    def get_customer_by_id(self,customerId:int):
        try:
            return self.service.find_customer_by_id(customerId)
        except CustomerError as e:
            print(f"Customer Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        

    def get_all_customer(self):
        try:
            return self.service.get_all_customers()
        except Exception as e:
            print(f"Unexpected Error: {e}")

    def update_customer(self,customer:Customer):
        try:
            return self.service.update_customer(customer)
        except CustomerError as e:
            print(f"Customer Error: {e}")
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    def delete_customer(self,customerId:int):
        try:
            return self.service.delete_customer(customerId)
        except CustomerError as e:
            print(f"Customer Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

