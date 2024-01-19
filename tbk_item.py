import tbk_ui
from tabulate import tabulate
import tbk_job


class Shop:
    def __init__(self, items=None, loc_x=0, loc_y=0):
        if items is None:
            items = []
        self.items = items
        self.loc_x = loc_x
        self.loc_y = loc_y


class Item:
    def __init__(self, name, purchase_price, sale_price, quantity):
        self.name = name
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.quantity = quantity


class Consumable(Item):
    def __init__(self, name, purchase_price, sale_price, quantity, category, value):
        Item.__init__(self, name, purchase_price, sale_price, quantity)
        self.category = category
        self.value = value


class Equipment(Item):
    def __init__(self, name, purchase_price, sale_price, quantity, job_category_id):
        Item.__init__(self, name, purchase_price, sale_price, quantity)
        self.job_category_id = job_category_id


class Weapon(Equipment):
    def __init__(self, name, purchase_price, sale_price, quantity, job_category_id, attack):
        Equipment.__init__(self, name, purchase_price,
                           sale_price, quantity, job_category_id)
        self.attack = attack


class Armor(Equipment):
    def __init__(self, name, purchase_price, sale_price, quantity, job_category_id, defense):
        Equipment.__init__(self, name, purchase_price,
                           sale_price, quantity, job_category_id)
        self.defense = defense


class Jewel(Equipment):
    def __init__(self, name, purchase_price, sale_price, quantity, job_category_id, defense):
        Equipment.__init__(self, name, purchase_price,
                           sale_price, quantity, job_category_id)
        self.defense = defense


potion = Consumable("Potion", 50, 25, 1, "heal", 25)
beer = Consumable("Beer", 50, 25, 1, "heal", 100)
antidote = Consumable("Antidote", 50, 25, 1, "cure", 0)

sword = Weapon("Sword", 50, 25, 1, tbk_job.TYPE_FIGHT, 5)
bow = Weapon("Bow", 50, 25, 1, tbk_job.TYPE_RANGE, 10)

shield = Armor("Shield", 50, 25, 1, tbk_job.TYPE_FIGHT, 5)
ring = Jewel("Ring", 50, 25, 1, tbk_job.TYPE_FIGHT, 5)

list_shop = [
    potion,
    beer,
    antidote,
    sword,
    bow,
    shield,
    ring
]
shop = Shop(list_shop, 1, 0)


list_weapon_name = [
    "dagger",
    "katana",
    "sword",
    "hammer",
    "knife",
    "battleaxe",

]
list_armor_name = [
    "shield",
    "helmet",
]


def create_item() -> str:
    text = ""
    for weapon_name in list_weapon_name:
        text += weapon_name + " = " + "tbk_item.Weapon('" + weapon_name.capitalize() + "',50,25,1,tbk_job.TYPE_FIGHT,10)" + "\r"

    text += "\r"
    for armor_name in list_armor_name:
        text += armor_name + " = " + "tbk_item.Armor('" + armor_name.capitalize() +  "',50,25,1,tbk_job.TYPE_FIGHT,10)" + "\r"

    with open('items.py', 'a', encoding="utf-8") as file:
        file.write(text)


def compare_item(item1, item2):
    headers = ["Fields", item1.name, item2.name]
    table = []

    if isinstance(item1, Weapon) and isinstance(item2, Weapon):
        table.append(["Attack", item1.attack, compare(item1.attack,item2.attack)])
        print(tabulate(table, headers, tablefmt="pretty"))
    elif isinstance(item1, (Armor, Jewel)) and isinstance(item2, (Armor, Jewel)):
        table.append(["Defense", item1.defense,compare(item1.defense, item2.defense)])
        print(tabulate(table, headers, tablefmt="pretty"))
    else:
        print("No comparison!")


def compare(value1, value2):
    text = value2
    if value1 < value2:
        text = tbk_ui.GREEN + str(text) + tbk_ui.END
    elif value1 > value2:
        text = tbk_ui.RED + str(text) + tbk_ui.END
    return text


compare_item(ring, ring)
