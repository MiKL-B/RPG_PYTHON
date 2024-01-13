import module_ui
from PNJ import list_pnj
from Boss import list_boss


class Location():
    def __init__(self, index, name, positionY, positionX, shop):
        self._index = index
        self._name = name
        self._positionY = positionY
        self._positionX = positionX
        self._shop = shop


# #--------------------------------------------------------------------

plaine = Location("00", "plaine", 0, 0, False)
plaine2 = Location("10", "plaine 2", 1, 0, False)
ville = Location("20", "ville", 2, 0, True)
ville2 = Location("25", "ville2", 2, 5, False)

list_locations = [[plaine, plaine2, ville, ville2]]
a_lists = [list_locations, list_pnj, list_boss]
# #   x -> 0, 1, 2, 3
# # y
# # 0     00, 01, 02, 03
# # 1     10, 11, 12, 13
# # 2     20, 21, 22, 23
# # 3     30, 31, 32, 33
# #--------------------------------------------------------------------
# array of world map and switch on them for a larger world


def display_world_map(player_positionY, player_positionX):
    world_map = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
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
    display_info_map(player_positionY, player_positionX)
    print_map(world_map, player_positionY, player_positionX)
# #--------------------------------------------------------------------


def print_map(world_map, player_positionY, player_positionX):
    for index, item in enumerate(a_lists):
        for jindex, jitem in enumerate(item):
            for key, value in enumerate(item[jindex]):
                x = value._positionX
                y = value._positionY
                world_map[y][x] = value._index

    # player position on the map
    world_map[player_positionY][player_positionX] = module_ui.GREEN + " P " + module_ui.END

    iLength = 11
    for i in world_map:
        print('\n' + '+---' * iLength + '+')
        for j in i:
            print('|{:^3}'.format(j), end='')
        print('|', end='')
    print('\n' + '+---' * iLength + '+')

# #--------------------------------------------------------------------

def display_info_map(player_Y, player_X):
    s_name = "Unknown"
    for index, item in enumerate(a_lists):
        for jindex, jitem in enumerate(item):
            for key, value in enumerate(item[jindex]):
                if player_Y == value._positionY and player_X == value._positionX:
                    s_name = value._name
    print(s_name)

# #--------------------------------------------------------------------


def is_player_in_town(player_Y, player_X):
    for index, item in enumerate(list_locations):
        for key, value in enumerate(list_locations[index]):
            if player_Y == value._positionY and player_X == value._positionX and value._shop:
                return value._shop


def is_player_on_pnj(player_Y, player_X):
    for index, item in enumerate(list_pnj):
        for key, value in enumerate(list_pnj[index]):
            if player_Y == value._positionY and player_X == value._positionX:
                return True


def is_player_on_boss(player_Y, player_X):
    for index, item in enumerate(list_boss):
        for key, value in enumerate(list_boss[index]):
            if player_Y == value._positionY and player_X == value._positionX:
                return True



def is_player_on_position(player_Y, player_X):
    for index, item in enumerate(a_lists):
        for jindex, jitem in enumerate(item):
            for key, value in enumerate(item[jindex]):
                if player_Y == value._positionY and player_X == value._positionX:
                    return True

# #--------------------------------------------------------------------
