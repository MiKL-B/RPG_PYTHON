"""item"""
import module_ui


class Item:
    """item"""

    def __init__(self, name, level, description, purchase_price, sales_price):
        self.name = name
        self.level = level
        self.description = description
        self.purchase_price = purchase_price
        self.sales_price = sales_price


class Consumable(Item):
    def __init__(self, name, level, description, purchase_price, sales_price, effect):
        Item.__init__(self, name, level, description,
                      purchase_price, sales_price)
        self.effect = effect


class Weapon(Item):
    def __init__(self, name, level, description, purchase_price, sales_price, attack):
        Item.__init__(self, name, level, description,
                      purchase_price, sales_price)
        self.attack = attack


class Armor(Item):
    def __init__(self, name, level, description, purchase_price, sales_price, defense):
        Item.__init__(self, name, level, description,
                      purchase_price, sales_price)
        self.defense = defense


beer = Consumable("Beer", 1, "An IPA beer", 25, 0, "give 50 HP")
sword = Weapon("Sword", 1, "A woodstick", 20, 10, 0)
potion = Consumable("Potion", 1, "A little potion", 50, 0, "give 20 HP")
shield = Armor("Shield", 2, "A round wooden table", 200, 10, 0)
shop = [
    potion,
    shield,
    sword,
    beer
]

def make_reduction(percentage):
    """make reduction"""
    for item in shop:
        reduction = item.purchase_price * (percentage / 100)
        item.sales_price = item.purchase_price - reduction

make_reduction(30)

def refresh_shop():
    """refresh shop item"""
    for item in shop:
        print(f"Name: {module_ui.color(item.name,'green')}")
        print(f"Description : {module_ui.color(item.description,'green')}")
        print(f"Price: {module_ui.color(item.purchase_price,'yellow')} gold")
        if hasattr(item, 'defense'):
            print(f"Defense: {module_ui.color(item.defense,'green')}")
        elif hasattr(item, 'attack'):
            print(f"Attack: {module_ui.color(item.attack,'green')}")
        elif hasattr(item, 'effect'):
            print(f"Effect: {module_ui.color(item.effect,'green')}")
        print("_____________________")
        print("\r")
