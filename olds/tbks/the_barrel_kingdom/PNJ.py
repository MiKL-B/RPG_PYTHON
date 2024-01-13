from Character import Character


class PNJ(Character):
    def __init__(self, name, level, health, max_health, mana, max_mana,
                 strength, defense, speed, positionX, positionY, index):
        Character.__init__(
            self, name, level, health, max_health, mana, max_mana, strength,
            defense, speed, positionX, positionY)
        self._index = index


pnj = PNJ(
    "Jean", "level", "health", "max_health", "mana", "max_mana", "strength",
    "defense", "speed", 3, 3, "33")

list_pnj = [[pnj]]
