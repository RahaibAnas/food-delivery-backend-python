from exceptions import *

class Customer:
    def __init__(self,id:int,name:str,PhoneNumber:str,email:str,password:str):
        self.id = id
        self.name = name
        self.phone_number = PhoneNumber
        self.email = email
        self.password = password


    def __str__(self):
        return(
            f"Id: {self.id}\n"
            f"Name: {self.name}\n"
            f"Phone Number: {self.phone_number}\n"
            f"Email: {self.email}\n"
            f"Password: {self.password}"
        )
    
    def verify_password(self,password:str):
        return self.password == password

        
    def change_password(self,oldPassword:str,newPassword:str):
        if self.password == oldPassword:
            self.password = newPassword
            return newPassword
        raise InvalidPasswordError("Invalid Password")
        
        
    def to_dict(self):
        return{
            "Id" : self.id,
            "Name": self.name,
            "Phone Number": self.phone_number,
            "Email": self.email,
            "Password": self.password
        }

    @classmethod
    def from_dict(cls,data):
        return cls(
            data["Id"],
            data["Name"],
            data["Phone Number"],
            data["Email"],
            data["Password"]
        )
    





        