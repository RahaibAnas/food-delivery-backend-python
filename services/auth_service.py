from repositories.owner_repository import OwnerRepository
from models.owner import Owner

from exceptions import *

class AuthService:
    def __init__(self,ownerRepository:OwnerRepository):
        self.repository = ownerRepository
        self.current_user = None
        

    def register(self,owner:Owner):
        self._validate_owner(owner)
        self.repository.save(owner)
        return owner

    def login(self,email:str,password:str):
        self._validate_email(email)
        self._validate_password(password)
        owner = self.repository.find_by_email(email)
        if owner:
            if owner.verify_password(password):
                self.current_user = owner
                return self.current_user
        raise InvalidCredentialsError("Invalid Email or Password")

    def logout(self):
        if self.current_user:
            self.current_user = None
            return
        raise loginRequiredError("Login Required")
    
    def change_password(self,oldPassword:str,newPassword:str):
        user = self.repository.find_by_id(self.get_current_user().id)
        if user:
            user.change_password(oldPassword,newPassword)
            self.repository.update(user)
            return
        raise loginRequiredError("Login Required")
        

        

    def get_current_user(self):
        if self.current_user:
            return self.current_user
        raise loginRequiredError("Login Required")

    def is_logged_in(self):
        if self.current_user:
            return True


    def _validate_owner(self,owner:Owner):
        self._check_duplicate(owner)
        self._validate_email(owner.email)
        self._validate_password(owner.password)
        if not len(owner.phone_number) == 11 or not owner.phone_number.isdigit():
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


    def _check_duplicate(self,owner:Owner):
        own1 = self.repository.find_by_id(owner.id)
        own2 = self.repository.find_by_email(owner.email)
        if own1 or own2:
            raise OwnerDuplicateError("Owner Exists")

    


