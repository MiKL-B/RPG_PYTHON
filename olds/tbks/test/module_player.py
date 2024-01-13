import time

import module_ui
import i18n.module_text as module_text
from module_character import Character


class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self._experience = 0
        self._max_experience = 10
        self._skill_point = 0
        self._abilities = []
        self._gold = 100
        self._inventory = []
        self._quests = []
        self._equipment_set = []
        self._bestiary = []
        self._weapon = []


    def set_default_name(self):
        self._name = "Dwarf"


    def set_test_values(self):
        self._name = "Dwarf"
        self._level = 25
        self._health = 2375
        self._max_health = 3500
        self._strength = 140
        self._defense = 200
        self._speed = 125
        self._y = 10
        self._x = 25
        self._experience = 9670
        self._max_experience = 10000
        self._skill_point = 16
        self._abilities = ["Fire"]
        self._gold = 2540
        self._inventory = ["Potion"]
        self._quests = ["Quest 1"]
        self._equipment_set = ["Helmet"]
        self._bestiary = ["Gobelin"]
        self._weapon = ["Sword"]


    def info(self):
        super().info()
        print(f"Exp: {self.get_experience()}")
        print(f"{self.get_position()}")
        module_ui.print_separator()
        print(f"Gold: {self.get_gold()}")


    def info_equipment(self):
        self.get_equipment_set()


    def info_inventory(self):
        self.get_inventory()


    def info_quests(self):
        print(f"Quest: {self.get_quests()}")


    def info_bestiary(self):
        print(f"Bestiary: {self.get_bestiary()}")


    def info_skills(self):
        print(f"Skill point: {self.get_skill_point()}")
        print(f"Abilities: {self.get_abilities()}")


    def increase_level(self):
        if self._experience == self._max_experience:
            self._level += 1


    def get_experience(self):
        return str(self._experience) + " / " + str(self._max_experience)


    def increase_experience(self, value):
        self._experience += value


    def get_skill_point(self):
        return self._skill_point


    def increase_skill_point(self, value):
        self._skill_point += value


    def decrease_skill_point(self, value):
        self._skill_point -= value


    def reset_skill_point(self):
        self._skill_point = self._level


    def get_abilities(self):
        return self._abilities


    def increase_strength(self, value):
        self._strength += value


    def decrease_strength(self, value):
        self._strength -= value


    def increase_defense(self, value):
        self._defense += value


    def decrease_defense(self, value):
        self._defense -= value


    def get_position(self):
        return "Y: "+ str(self._y) + " | X: " + str(self._x)


    def print_position(self):
        print(f"Y: "+ str(self._y) + " | X: " + str(self._x))


    def move(self, y, x):
        self._y += y
        self._x += x


    def move_top(self):
        if self._y > 0:
            self.move(-1, 0)
        else:
            print("you can not go here")
            time.sleep(2)


    def move_left(self):
        if self._x > 0:
            self.move(0, -1)
        else:
            print("you can not go here")
            time.sleep(2)


    def move_bottom(self):
        self.move(1, 0)


    def move_right(self):
        self.move(0, 1)


    def get_gold(self):
        return self._gold


    def increase_gold(self, value):
        self._gold += value


    def decrease_gold(self, value):
        if self._gold > 0:
            self._gold -= value


    def get_inventory(self):
        if len(self._inventory) > 0:
            print(self._inventory)
        else:
            module_ui.print_message(module_text.INVENTORY_EMPTY)


    def get_quests(self):
        return self._quests


    def get_equipment_set(self):
        self.get_weapons()
        # self.get_shield()
        # self.get_equipement()


    def get_weapons(self):
        print("Weapons: ")
        for index, item in enumerate(self._weapon):
            print("")
            print(item._name)
            print(f"+ {item._strength} strength")


    def equip_weapons(self, item):
        if len(self._weapon) < 1:
            self._weapon.append(item)
            self._strength += item._strength


    def unequip_weapons(self, item):
        if len(self._weapon) > 0:
            self._weapon.remove(item)
            self._strength -= item._strength


    def get_bestiary(self):
        return self._bestiary
