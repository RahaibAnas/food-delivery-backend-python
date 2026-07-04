class MenuItem:
    def __init__(self,id:int,name:str,description:str,price:float,avaliable:bool,prepare_time:int):
        self.id = id
        self.name = name
        self.description = description
        if price > 0:
            raise ValueError("Value must be greater than zero")
        self.price = price
        self.avaliable = avaliable
        self.preparation_time = prepare_time

    def __str__(self):
        return(
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Price: {self.price}\n"
            f"Avalibility: {self.avaliable}\n"
            f"Preparation_time: {self.preparation_time}"
        )
    
    def change_price(self,new_price:float):
        if new_price > 0:
            self.price = new_price
            print("Price change")
        else:
            print("Price must be greater than Zero")

    def enable(self):
        if self.avaliable:
            pass
        else:
            self.avaliable = True

    def disable(self):
        if self.avaliable:
            self.avaliable = False
        else:
            pass

    def update_description(self,new_description:str):
        self.description = new_description
        print("Description change")


