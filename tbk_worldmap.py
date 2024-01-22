import tbk_location
import tbk_ui

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

def print_zone(worlds,pworldy,pworldx,plocy,plocx):
    text_world = "Unknown"
    text_local = "Unknown"
    for world in worlds:
        if world.x == pworldx and world.y == pworldy:
            text_world = world.name
        for location in world.locations:
            if location.x == plocx and location.y == plocy:
                text_local = location.name
    tbk_ui.print_msg("World",text_world,"green")
    tbk_ui.print_msg("Local",text_local,"green")

def display(player_world_y, player_world_x, player_location_y, player_location_x):
    """display map"""

    zone1 = WorldMap("zone1", 0, 0)
    zone2 = WorldMap("zone2", 0, 1)

    zone1.locations = [
        tbk_location.swamp,
        tbk_location.town,
        tbk_location.test,
        tbk_location.change
    ]
    zone2.locations = [
        tbk_location.test
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

    print_map(worlds, player_world_y, player_world_x,player_location_y, player_location_x)
    print_zone(worlds, player_world_y, player_world_x,player_location_y, player_location_x)

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
