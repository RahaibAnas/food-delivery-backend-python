class Owner:
    def __init__(self,id:int,name:str,phoneNumber:str,email:str):
        self.id = id
        self.name = name
        self.__phone_number = phoneNumber
        self.email = email

    def __str__(self):
        return(
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Phone Number: {self.__phone_number}\n"
            f"Email: {self.email}"
        )
    
    def update_info(self,name:str|None="",PhoneNumber:str|None = None,email:str|None = ""):
        if name:
            self.name = name
            print("Name Changed")
        if PhoneNumber:
            self.__phone_number = PhoneNumber
            print("Phone Number Changed")
        if email:
            self.email = email
            print("Email Changed")



