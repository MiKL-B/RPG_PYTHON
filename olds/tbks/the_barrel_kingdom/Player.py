import module_ui
from Character import Character
from Singleton import SingletonMeta
from rich.table import Table
from rich.console import Console

class Player(Character, metaclass=SingletonMeta):
    def __init__(self, name="Dwarf", level=1, health=50, max_health=50, mana=10, max_mana=10, strength=1,
                 defense=1, speed=1, positionX=0, positionY=0, gold=500,
                 inventory=[], experience=0, max_experience=100, skill_point=0, quests=[]):
        Character.__init__(self, name, level, health, max_health, mana,
                           max_mana, strength, defense, speed, positionX, positionY)
        self._gold = gold
        self._inventory = inventory
        self._experience = experience
        self._max_experience = max_experience
        self._skill_point = skill_point
        self._quests = quests
        # self._abilities


    def print_info(self):
        super().print_info()
        module_ui.print_separator()
        print(f"Skill point: {module_ui.return_text(self._skill_point, module_ui.CYAN)}")
        print(f"Experience: {module_ui.return_text(self._experience, module_ui.CYAN)} / {module_ui.return_text(self._max_experience,module_ui. CYAN)}")
        module_ui.print_separator()
        self.display_position()
        module_ui.print_separator()
        self.display_gold()


    def set_default_value(self):
        self._name = "Dwarf"
        self._level = 1
        self._health = 50
        self._max_health = self._health
        self._mana = 10
        self._max_mana = 10
        self._strength = 1
        self._defense = 1
        self._speed = 1
        self._positionX = 0
        self._positionY = 0
        self._gold = 500
        self._inventory = []
        self._experience = 0
        self._max_experience = 100
        self._skill_point = 0
        self._quests = []


    def display_position(self):
        print(f"Y: {self._positionY} | X: {self._positionX}")


    def display_info_combat(self):
        super().display_info_combat()


    def display_gold(self):
        print(f"Gold: {module_ui.return_text(self._gold, module_ui.YELLOW)}")


    def display_inventory(self):
        if len(self._inventory) > 0:
            table_inventory = Table(title="Inventory")
            table_inventory.add_column("Index")
            table_inventory.add_column("Name")
            table_inventory.add_column("Description")  # description
            table_inventory.add_column("Category")  # type

            table_inventory.add_column("Quantity", justify="right")  # quantity
            table_inventory.add_column(
                "Sale price", justify="right")  # sale price
            table_inventory.add_column(
                "Total sale price", justify="right")  # total sale price
    #       quantity = 1
    #       if not self.has_inventory_empty():
    #             for index, item in enumerate(self._inventory):
    #                 if self._inventory[index] in self._inventory[index+1:]:
    #                     item._quantity += quantity
    #                 else:
    #                     list_objects.add_row(item._name,item._category,item._description,str(item._quantity),str(item._sales_price),str(item._sales_price * item._quantity))
    #             console = Console()
    #             console.print(list_objects)
    #         else:
    #             print("your inventory is empty")
            for index, item in enumerate(self._inventory):
                table_inventory.add_row(
                    str(item._index), item._name,
                    item._description, item._category)
            console = Console()
            console.print(table_inventory)
        else:
            print(f"Inventory empty")

    def has_inventory_full(self):
        return 9 < len(self._inventory) < 11

    def has_inventory_empty(self):
        return len(self._inventory) == 0

    def buy_item(self, item):
        if self.has_inventory_full():
            print("inventory full")
        else:
            if self.has_enough_gold(item._price):
                self.decrease_gold(item._price)
                self._inventory.append(item)
                print(f"you have bought: {item._name}")
                wait(2)
            else:
                print("you have not enough gold.")

    def sell_item(self, item):
        if self.has_inventory_empty():
            print(f'your inventory is empty')
        else:
            self.increase_gold(item._price)
            self._inventory.remove(item)
            print(f"you have sold: {item._name}")
            wait(2)

    def has_enough_gold(self, amount):
        if self._gold >= amount:
            enough_gold = True
        else:
            enough_gold = False
        return enough_gold

    def decrease_gold(self, amount):
        if self._gold > 0:
            self._gold -= amount

    def increase_gold(self, amount):
        self._gold += amount

    def pickup_item(self, item):
        if len(self._inventory) <= 10:
            self._inventory.append(item)
        else:
            print("you have your inventory full")

    def throw_item(self, item):
        if len(self._inventory) > 0:
            self._inventory.remove(item)
            item._quantity -= 1
        else:
            print("your inventory is empty")

    def increase_level(self):
        if self._experience == self._max_experience:
            self._level += 1
            print_message("Level up !", GREEN)
            print(
                f"Level: {self._level - 1} -> {return_text(self._level, GREEN)}")
            self.increase_stat()
            self.increase_skill_point()

    def increase_skill_point(self):
        self._skill_point += 1

    def increase_stat(self):
        self._health += 20
        self._max_health = self._health
        print(
            f"Health: {self._max_health - 20} -> {return_text(self._max_health, GREEN)}")

    def reset_skill_point(self):
        self._skill_point = self._level

    def is_alive(self):
        return self._health > 0

    def die(self):
        self._health = 0

    def is_level_up(self):
        return self._experience == self._max_experience

    def move(self, y, x):
        self._positionY += y
        self._positionX += x

    def move_north(self):
        if self._positionY > 0:
            self.move(-1, 0)
        else:
            print("you can not go here")
            module_ui.wait(2)

    def move_west(self):
        if self._positionX > 0:
            self.move(0, -1)
        else:
            print("you can not go here")
            module_ui.wait(2)

    def move_south(self):
        if self._positionY < 10:
            self.move(1, 0)
        else:
            print("you can not go here")
            module_ui.wait(2)

    def move_east(self):
        if self._positionX < 10:
            self.move(0, 1)
        else:
            print("you can not go here")
            module_ui.wait(2)

    def increase_experience(self, amount):
        self._experience += amount

    def get_reward(self, amount, item):
        self.increase_experience(amount)
        if item != None:
            self.pickup_item(item)
        if self.is_level_up():
            self.increase_level()

    def use_item(self, item):  # manage quantity for object
        self._health += item._amount
        print(f"{self._health - item._amount} -> {self._health}")
        self._inventory.remove(item)
        wait(2)

    # def flee(self):
    #     pass

    # def parry(self):
    #     pass
# #--------------------------------------------------------------------
# #----------------------QUESTS----------------------------------------
# #--------------------------------------------------------------------

    def sheet_quests(self):
        list_quests = Table(title="quests")  # quests
        list_quests.add_column("name")  # name
        list_quests.add_column("Description")  # description
        # list_quests.add_column("status") # status
        # list_quests.add_column("reward",justify="right") # reward

        if len(self._quests) > 0:
            for index, item in enumerate(self._quests):
                list_quests.add_row(item._name, item._description)
            console = Console()
            console.print(list_quests)
        else:
            print("your quests list is empty")

# #--------------------------------------------------------------------

    def pickup_quest(self, quest):
        if self.has_quests_full():
            print("you have your quests full")
        else:
            self._quests.append(quest)

# #--------------------------------------------------------------------

    def throw_quest(self, quest):
        if self.has_quests_empty():
            print("you have not quests")
        else:
            self._quests.remove(quest)

# #--------------------------------------------------------------------

    def has_quests_full(self):
        return 9 < len(self._quests) < 11

# #--------------------------------------------------------------------

    def has_quests_empty(self):
        return len(self._quests) == 0
