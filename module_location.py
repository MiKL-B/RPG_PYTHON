"""module location"""


class Location:
    """class location"""

    def __init__(self, index, name, y, x, shop=False):
        self.index = index
        self.name = name
        self.x = x
        self.y = y
        self.shop = shop


swamp = Location("00", "Swamp", 0, 0)
town = Location("10", "Town", 1, 0, True)
test = Location("100", "Town", 10, 0, True)
change = Location("c", "Change", 10, 5)
locations = [
    swamp,
    town,
    test,
    change
]
