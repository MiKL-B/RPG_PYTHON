import location.module_location as module_location


class WorldMap:
    def __init__(self, name="", x=0, y=0, wmap=None, locations=None):
        self.name = name
        self.x = x
        self.y = y
        if wmap is None:
            wmap = []
        self.wmap = wmap

        if locations is None:
            locations = []
        self.locations = locations


def display(player_world_y, player_world_x, player_location_y, player_location_x):
    """display map"""

    zone1 = WorldMap("zone1", 0, 0)
    zone2 = WorldMap("zone2", 0, 1)

    zone1.locations = [
        module_location.swamp,
        module_location.town,
        module_location.test,
        module_location.change
    ]
    zone2.locations = [
        module_location.test
    ]

    worlds = [zone1, zone2]

    for world in worlds:
        world.wmap = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    print_map(worlds, player_world_y, player_world_x,
              player_location_y, player_location_x)


def print_map(worlds, player_world_y, player_world_x, player_location_y, player_location_x):
    """print map"""
    # display locations on the map
    for world in worlds:
        for loc in world.locations:
            x = loc.x
            y = loc.y
            world.wmap[y][x] = loc.index

        # display the player
        world.wmap[player_location_y][player_location_x] = " P "

        # draw the map
        columns = 11
        if world.x == player_world_x and world.y == player_world_y:
            for i in world.wmap:
                print('\n' + '+---' * columns + '+')
                for j in i:
                    print('|{:^3}'.format(j), end='')
                print('|', end='')
            print('\n' + '+---' * columns + '+')
            print(f"World:{world.name}")
            print(f"X:{world.x} Y:{world.y}")
