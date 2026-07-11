from models.customer import Customer
from repositories.customer_repository import CustomerRepository

from exceptions import *

class CustomerService:
    def __init__(self,customerRepository:CustomerRepository):
        self.repository = customerRepository

    def register(self,customer:Customer):
        self._validate_customer(customer)
        self.repository.save(customer)
        return customer
    
    def get_all_customers(self):
        data = self.repository.get_all()
        return data
    
    def find_customer_by_id(self,customerId:int):
        cust = self.repository.find_by_id(customerId)
        if cust:
            return cust
        raise CustomerNotFoundError("Customer not found")
        
    def update_customer(self,customer:Customer):
        cust = self.repository.find_by_id(customer.id)
        if cust:
            self._validate_customer(customer)
            self.repository.update(customer)
            return customer
        raise CustomerNotFoundError("Customer Not found")
    
    def delete_customer(self,customerId:int):
        cust = self.repository.find_by_id(customerId)
        if cust:
            self.repository.delete(customerId)
            return customerId
        raise CustomerNotFoundError("Customer Not found")





















    def _validate_customer(self,customer:Customer):
        self._check_duplicate(customer)
        self._validate_email(customer.email)
        self._validate_password(customer.password)
        if not len(customer.phone_number) == 11 or not customer.phone_number.isdigit():
            raise InvalidPhoneError("Invalid Phone Number")

    def _validate_email(self,email:str):
        if not email.endswith("@gmail.com"):
                raise InvalidEmailError("Invalid Email")

        if " " in email:
                raise InvalidEmailError("Email cannot contain spaces")

    


    def _validate_password(self,password:str):
        has_upper = False 
        for p in password:
            if  p.isupper():
                has_upper = True
                break     
        has_lower =False
        for p in password:
            if  p.islower():
                has_lower = True
                break            
        has_digit =False
        for p in password:
            if  p.isdecimal():
                has_digit = True
                break
        has_symbol=False
        for p in password:
            if p  in "!@#$%^&*<>?/|":
                 has_symbol = True
                 break
        if not has_upper or not has_lower or not has_digit or not has_symbol or len(password) < 8:
            raise InvalidPasswordError("Invalid Password")


    def _check_duplicate(self,customer:Customer):
        own1 = self.repository.find_by_id(customer.id)
        own2 = self.repository.find_by_email(customer.email)
        own3 = self.repository.find_by_phone(customer.phone_number)
        if own1 or own2 or own3:
            raise CustomerDuplicateError("Customer Exists")