
# def main(self):
option_load = [
    "Load"
    ,"Delete"
    ,"Quit"
]
function_load = [
    "self.load_player(), self.game()"
    ,"module_data.delete(), time.sleep(2), self.main()"
    ,"self.quit()"
]

option_new = [
    "New"
    ,"Quit"
]
function_new = [
    "self.new_player(), self.game()"
    ,"self.quit()"
]

# def game(self):
option_game = [
    "Top"
    ,"Left"
    ,"Bottom"
    ,"Right"
    ,""
    ,"Character"
    ,"Options"
]
function_game = [
    "self._hero.move_top(), self.game()"
    ,"self._hero.move_left(), self.game()"
    ,"self._hero.move_bottom(), self.game()"
    ,"self._hero.move_right(), self.game()"
    ,""
    ,"self.display_menu_character()"
    ,"self.display_menu_options()"
]

# def display_options(self):
option_options = [
    "Return"
    ,""
    ,"Save"
    ,"Main"
    ,"Quit"
]
function_options = [
    "self.game()"
    ,""
    ,"self.display_menu_save()"
    ,"self.main()"
    ,"self.quit()"
]

# def display_menu_save(self):
option_return = [
    "Return"
]
function_return = [
    "self.game()"
]

# def display_menu_character(self):
option_character = [
    "Return"
    ,"Inventory"
    ,"Quests"
    ,"Skills"
]
function_character = [
    "self.game()"
    ,"self.display_menu_inventory()"
    ,""
    ,""
]
