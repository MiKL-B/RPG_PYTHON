class Item:
    def __init__(self, name):
        self._name = name


class Weapon(Item):
    def __init__(self, name, strength):
        Item.__init__(self, name)
        self._strength = strength


class Equipment(Item):
    def __init__(self, name, defense):
        Item.__init__(self, name)
        self._defense = defense



sword = Weapon("sword",1)
helmet = Equipment("helmet",1)
shield = Equipment("shield",1)
