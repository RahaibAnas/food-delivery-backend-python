from repositories.owner_repository import OwnerRepository
from models.owner import Owner

class AuthService:
    def __init__(self,ownerRepository:OwnerRepository):
        self.repository = ownerRepository
        self.current_user = None
        

    def register(self,owner:Owner):
        self._validate_owner(owner)

        self.repository.save(owner)
        print("Owner Registered")

    def login(self,email:str,password:str):
        self._validate_email(email)
        self._validate_password(password)
        owner = self.repository.find_by_email(email)
        if owner:
            if owner.password == password:
                self.current_user = owner.to_dict()
                print("login Successful")
                return self.current_user
        raise ValueError("Invalid Email or Password")

    def logout(self):
        if self.current_user:
            self.current_user = None
            print("Logged out")
            return
        raise ValueError("No User is logged in")
        

    def get_current_user(self):
        if self.current_user:
            return self.current_user
        raise ValueError("No user Logged in.")

    def is_logged_in(self):
        if self.current_user:
            return self.current_user


    def _validate_owner(self,owner:Owner):
        self._check_duplicate(owner)
        self._validate_email(owner.email)
        self._validate_password(owner.password)
        if len(owner.phone_number) < 11:
            raise ValueError("Invalid Phone Number")

    def _validate_email(self,email:str):
        if not email.endswith("@gmail.com"):
                raise ValueError("Invalid Email")

        if " " in email:
                raise ValueError("Email cannot contain spaces")


    def _validate_password(self,password:str):
        a = False 
        for p in password:
            if  p.isupper():
                a = True
                break     
        b=False
        for p in password:
            if  p.islower():
                b = True
                break            
        c=False
        for p in password:
            if  p.isdecimal():
                c = True
                break
        d=False
        for p in password:
            if p  in "!@#$%^&*<>?/|":
                 d = True
                 break
        if not a or not b or not c or not d or len(password) < 8:
            raise ValueError("Invalid Password")


    def _check_duplicate(self,owner:Owner):
        own1 = self.repository.find_by_id(owner.id)
        own2 = self.repository.find_by_email(owner.email)
        if own1 or own2:
            raise ValueError("Owner Exists")


