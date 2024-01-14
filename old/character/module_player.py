"""module player"""
from tbk_singleton import Singleton
import module_ui
import module_text
from module_location import locations
import module_item


class Player(metaclass=Singleton):
    """class player"""

    def __init__(self, heroes=None, inventory=None, quests=None, gold=2000, world_map_x=0, world_map_y=0, location_x=0, location_y=0):
        if heroes is None:
            heroes = []
        self.heroes = heroes

        if inventory is None:
            inventory = []
        self.inventory = inventory

        if quests is None:
            quests = []
        self.quests = quests

        self.gold = gold
        self.world_map_x = world_map_x
        self.world_map_y = world_map_y
        self.location_x = location_x
        self.location_y = location_y

    def refresh(self):
        """refresh info player + heroes of player"""
        for hero in self.heroes:
            print(f"Name: {hero.name} Class: {hero.job}")
        print(f"Gold: {module_ui.color(self.get_gold(),'yellow')}")

    # region inventory
    def refresh_inventory(self):
        """refresh inventory"""
        if len(self.inventory) == 0:
            print(f"{module_ui.color(module_text.INVENTORY_EMPTY,'red')}")
            return

        for item in self.inventory:
            self.refresh_info_item(item)

    def refresh_equipable_items(self):
        """refresh equipable items"""
        for item in self.inventory:
            if isinstance(item, (module_item.Weapon, module_item.Armor)):
                self.refresh_info_item(item)

    def refresh_info_item(self, item):
        """refresh info item"""
        print(f"Name: {module_ui.color(item.name,'green')}")
        print(f"Description: {module_ui.color(item.description,'green')}")
        print(f"Price: {module_ui.color(item.sales_price,'yellow')} gold")
        if hasattr(item, 'defense'):
            print(f"Defense: {module_ui.color(item.defense,'green')}")
        elif hasattr(item, 'attack'):
            print(f"Attack: {module_ui.color(item.attack,'green')}")
        elif hasattr(item, 'effect'):
            print(f"Effect: {module_ui.color(item.effect,'green')}")
        print("_____________________")
        print("\r")

    def get_inventory(self):
        """get inventory"""
        return self.inventory
    # endregion

    # region buy & sell
    def get_gold(self):
        """get gold"""
        return self.gold

    def refresh_gold(self):
        """refresh gold"""
        print(f"Your gold: {module_ui.color(self.get_gold(),'yellow')}")

    def increase_gold(self, value):
        """increase gold"""
        self.gold += value

    def decrease_gold(self, value):
        """decrease gold"""
        self.gold -= value

    def buy_item(self, item):
        """buy item"""
        if self.gold < item.purchase_price:
            print(f"{module_ui.color(module_text.NOT_ENOUGH_MONEY,'red')}")
            return

        self.decrease_gold(item.purchase_price)
        self.inventory.append(item)
        print(f"{module_ui.color(module_text.BOUGHT,'green')} {item.name}!")

    def sell_item(self, item):
        """sell item"""
        self.increase_gold(item.sales_price)
        self.inventory.remove(item)
        print(f"{module_ui.color(module_text.SOLD,'green')} {item.name}!")
    # endregion

    def is_inventory_full(self) -> bool:
        """return inventory full or not"""
        return len(self.inventory) == 10

    def pickup_item(self, item):
        """pick up an item"""
        if not self.is_inventory_full():
            self.inventory.append(item)

    # region move
    def move(self, x, y):
        """move"""
        self.location_x += x
        self.location_y += y

        # change south
        if self.location_x == 5 and self.location_y == 10:
            self.change_zone(0, 1)
            self.location_x = 5
            self.location_y = 1
        # change north
        elif self.location_x == 5 and self.location_y == 0:
            self.change_zone(0, -1)
            self.location_x = 5
            self.location_y = 9
        # change east
        elif self.location_x == 10 and self.location_y == 5:
            self.change_zone(1, 0)
            self.location_x = 1
            self.location_y = 5
        # change west
        elif self.location_x == 0 and self.location_y == 5:
            self.change_zone(-1, 0)
            self.location_x = 9
            self.location_y = 5

    def change_zone(self, x, y):
        """change_zone"""
        self.world_map_x += x
        self.world_map_y += y

    def move_north(self):
        """move north"""
        if self.location_y > 0:
            self.move(0, -1)
        else:
            print(f"{module_ui.color(module_text.LOCATION_IMPOSSIBLE,'red')}")
            module_ui.wait()

    def move_west(self):
        """move west"""
        if self.location_x > 0:
            self.move(-1, 0)
        else:
            print(f"{module_ui.color(module_text.LOCATION_IMPOSSIBLE,'red')}")
            module_ui.wait()

    def move_east(self):
        """move east"""
        if self.location_x < 10:
            self.move(1, 0)
        else:
            print(f"{module_ui.color(module_text.LOCATION_IMPOSSIBLE,'red')}")
            module_ui.wait()

    def move_south(self):
        """move south"""
        if self.location_y < 10:
            self.move(0, 1)
        else:
            print(f"{module_ui.color(module_text.LOCATION_IMPOSSIBLE,'red')}")
            module_ui.wait()
    # endregion

    # region location
    def refresh_position(self):
        """refresh position"""
        location_name = module_text.UNKNOWN
        for item in locations:
            if item.x == self.location_x and item.y == self.location_y:
                location_name = item.name
        print(f"Local:{location_name}")
        print(f"X:{self.location_x} Y:{self.location_y}")

    def is_in_town(self) -> bool:
        """return if the player is in town for access to shop..."""
        in_town = False
        for item in locations:
            if item.x == self.location_x and item.y == self.location_y and item.shop:
                in_town = True
        return in_town
    # endregion


    def refresh_inventory(self):
        if len(self.inventory) == 0:
            print("Inventory empty!")
            return
        for item in self.inventory:
            print(item.name)
    
    def refresh_equipable_items(self):
        for item in self.inventory:
            if isinstance(item, (module_item.Weapon)):
                self.refresh_info_item(item)

    def get_list_equipable(self):
        list_items = []
        for item in self.inventory:
            if isinstance(item, (module_item.Weapon)):
                list_items.append(item)
        return list_items
                
    def refresh_info_item(self,item):
        print(item.name)

    def equip(self,item):
        self.inventory.remove(item)
        self.weapon = item

    def unequip(self,item):
        self.weapon = None 
        self.inventory.append(item)

    def get_weapon(self):
        if not self.weapon:
            print("No weapon!")
            return
        print(self.weapon.name)
