from Character import Character


class Boss(Character):
    def __init__(
       self, name, level, health, max_health, mana, max_mana, strength,
       defense, speed, positionX, positionY, index):
        Character.__init__(
                    self, name, level, health, max_health, mana, max_mana, strength,
                    defense, speed, positionX, positionY)
        self._index = index


boss = Boss(
    "Dwagon", "level", "health", "max_health", "mana", "max_mana", "strength",
    "defense", "speed", 6, 4, "64")

list_boss = [[boss]]
