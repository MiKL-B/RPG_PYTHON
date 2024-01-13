"""character"""


class Character:
    """class character"""

    def __init__(self, index: int, name: str,
                 level: int, health: int,
                 max_health: int, attack: int,
                 defense: int, magic: int, resource: int,
                 max_resource: int, x: int, y: int):
        self.index = index
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.resource = resource
        self.max_resource = max_resource
        self.x = x
        self.y = y
