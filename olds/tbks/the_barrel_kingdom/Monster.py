import module_ui
from Character import Character
import random
from Item import potion


class Monster(Character):
    def __init__(self, name, level, health, max_health, mana, max_mana,
                 strength, defense, speed, positionX, positionY, loot):
        Character.__init__(self, name, level, health, max_health, mana,
                           max_mana, strength, defense, speed,
                           positionX, positionY)
        self._loot = loot

    def print_info(self):
        super().print_info()
        print(f"Loot: {self._loot}")
        # print(self.__dict__)

    def display_info_combat(self):
        super().display_info_combat()


MONSTERS = [
    {
        "name": "Rat des égouts",
                "level": 1,
                "health": 50,
                "max_health": 50,
                "mana": 0,
                "max_mana": 0,
                "strength": 1,
                "defense": 5,
                "speed": 0,
                "loot": potion,
    },
    {
        "name": "Succube",
                "level": 1,
                "health": 50,
                "max_health": 50,
                "mana": 0,
                "max_mana": 0,
                "strength": 1,
                "defense": 5,
                "speed": 0,
                "loot": potion,
    },

]


def random_monster():
    rd_monster = random.choice(MONSTERS)
    monster = Monster(
        rd_monster['name'], rd_monster['level'], rd_monster['health'],
        rd_monster['max_health'], rd_monster['mana'], rd_monster['max_mana'],
        rd_monster['strength'], rd_monster['defense'], rd_monster['speed'],
        None, None, rd_monster['loot'])
    return monster
