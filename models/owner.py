class Owner:
    def __init__(self,id:int,name:str,phoneNumber:str,email:str,password:str):
        self.id = id
        self.name = name
        self.phone_number = phoneNumber
        self.email = email
        self.password = password

    def __str__(self):
        return(
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Phone Number: {self.phone_number}\n"
            f"Email: {self.email}"
        )
    
    def update_info(self,name:str|None="",PhoneNumber:str|None = None,email:str|None = ""):
        if name:
            self.name = name
            print("Name Changed")
        if PhoneNumber:
            self.phone_number = PhoneNumber
            print("Phone Number Changed")
        if email:
            self.email = email
            print("Email Changed")

    def verify_password(self,password:str):
        return self.password == password
            

    def change_password(self,oldPassword:str,newPassword:str):
        if self.password != oldPassword:
            raise ValueError("Incorrect Password")
        self.password = newPassword  
        print("Password changed")


    def to_dict(self):
        return{
            "Id": self.id,
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




