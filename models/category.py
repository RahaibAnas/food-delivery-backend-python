from .menu_item import MenuItem


class Category:
    def __init__(self,id:int,name:str) -> None:
        self.id = id
        self.name = name
        self.menu_items = []


    def add_item(self,*menuItem: MenuItem):
        for item in menuItem:
            self.menu_items.append(item)
        print("Item Added Successfully")

    def remove_item(self,id:int):
        for item in self.menu_items:
            if item.id == id:
                self.menu_items.remove(item)
                print("Item removed")
                return
            

    def find_item(self,id:int):
        for item in self.menu_items:
            if item.id == id:
                return item
            

    def show_items(self):
        print("="*20)
        print(f"Category: {self.name}")
        for item in self.menu_items:
            print("="*20)
            print(item)
        print("="*20)
        










