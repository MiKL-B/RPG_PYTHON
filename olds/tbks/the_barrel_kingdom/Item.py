class Item:
    def __init__(self, index, name, description, category, rarity, price):
        self._index = index
        self._name = name
        self._description = description
        self._category = category
        self._rarity = rarity
        self._price = price
        # self._quantity = quantity

    def get_type(self):
        return "item"


class Weapon(Item):
    def __init__(self, index, name, description, category, rarity, price,
                 strength):
        Item.__init__(self, index, name, description, category, rarity, price)
        self._strength = strength


class Equipment(Item):
    def __init__(self, index, name, description, category, rarity, price,
                 defense):
        Item.__init__(self, index, name, description, category, rarity, price)
        self._defense = defense


class Consumable(Item):
    def __init__(self, index, name, description, category, rarity, price,
                 amount):
        Item.__init__(self, index, name, description, category, rarity, price)
        self._amount = amount


# def display_rarity_name(item):
# 	if item._rarity == 0:
# 		color = ""
# 	if item._rarity == 1:
# 		color = "green"
# 	elif item._rarity == 2:
# 		color = "blue"
# 	elif item._rarity == 3:
# 		color = "magenta"
# 	name = "[bold "+ color +"]"+item._name+"[/bold "+ color+"]"
# 	return name
slip = Equipment(1, "Slip sale", "a slip", "equipment", 0, 10, 20)
potion = Consumable(2, "Potion de soin",
                    "Rend 10 pt de vie", "object", 1, 5, 10)
shield = Equipment(3, "Shield", "a shield", "equipment", 2, 10, 20)
sword = Weapon(4, "Sword de la destinÃ©e flamboyante sa mÃ¨re",
               "a sword", "weapon", 3, 10, 20)


aList_item = [slip, potion, shield, sword]
