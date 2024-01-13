class Shop:
    def __init__(self,items = None):
        if items is None:
            items = []
        self.items = items

class Item:
    def __init__(self,name):
        self.name = name

class Weapon(Item):
    def __init__(self,name):
        self.name = name

potion = Item("Potion")
sword = Weapon("Sword")


shop = Shop([potion,sword])