# options
YES = "Yes"
NO = "No"
NEW = "New"
LOAD = "Load"
DELETE = "Delete"
SAVE = "Save"
QUIT = "Quit"
HELP = "Help"
RETURN = "Return"
BUY = "Buy"
SELL = "Sell"
CHOOSE_QUEST = "Choose a quest"
END_GAME = "End game"
CHARACTER = "Character"
Z = "North"
Q = "West"
S = "South"
D = "East"
O = "Options"
INVENTORY = "Inventory"

# functions
s_main = "self.main()"
s_display_game = "self.display_game()"
s_new_game = "self.define_new_player(), self.intro_story()"
s_load_game = "self.load_game(), self.display_game()"
s_delete_game = "self.delete_game()"
s_save_game = "self.save_game()"
s_help = "self.display_help_menu()"
s_quit = "self.quit()"
s_delete = "self.delete()"
s_buy = "self.choose_item_to_buy()"
s_sell = "self.choose_item_to_sell()"
s_choose_quest = "self.choose_quest_to_accept()"
s_end_game = "self.end_game()"
s_sheet_hero = "self.sheet_hero()"
s_z = "self._hero.move_north(), self.random_combat(), self.display_game()"
s_q = "self._hero.move_west(), self.random_combat(), self.display_game()"
s_s = "self._hero.move_south(), self.random_combat(), self.display_game()"
s_d = "self._hero.move_east(), self.random_combat(), self.display_game()"
s_o = "self.display_menu_options()"
s_inventory = "self.display_menu_inventory()"

# menus
a_main_data = [
    {
        "text":LOAD,
        "code":"1",
        "function":s_load_game
    },
    {
        "text":DELETE,
        "code":"2",
        "function":s_delete_game
    },
    {
        "text":HELP,
        "code":"3",
        "function":s_help
    },
    {
        "text":QUIT,
        "code":"4",
        "function":s_quit
    },

]
a_main = [
    {
        "text":NEW,
        "code":"1",
        "function":s_new_game
    },
    {
        "text":HELP,
        "code":"2",
        "function":s_help
    },
    {
        "text":QUIT,
        "code":"3",
        "function":s_quit
    },
]
a_game = [
    {
        "text":CHARACTER,
        "code":"1",
        "function":s_sheet_hero
    },
    {
        "text":Z,
        "code":"z",
        "function":s_z
    },
    {
        "text":Q,
        "code":"q",
        "function":s_q
    },
    {
        "text":S,
        "code":"s",
        "function":s_s
    },
    {
        "text":D,
        "code":"d",
        "function":s_d
    },
    {
        "text":O,
        "code":"o",
        "function":s_o
    },
]
a_next = [
    {
        "text":YES,
        "code":"1",
        "function":s_display_game
    },
]

a_return_main = [
    {
        "text":RETURN,
        "code":"1",
        "function":s_main
    },
]
a_return_game = [
    {
        "text":RETURN,
        "code":"1",
        "function":s_display_game
    },
]
a_confirm_delete = [
    {
        "text":YES,
        "code":"1",
        "function":s_delete
    },
    {
        "text":NO,
        "code":"2",
        "function":s_main
    },
]

a_options = [
    {
        "text":RETURN,
        "code":"1",
        "function":s_display_game
    },
    {
        "text":SAVE,
        "code":"2",
        "function":s_save_game
    },
    {
        "text":QUIT,
        "code":"3",
        "function":s_quit
    },
]

a_sheet_hero = [
    {
        "text":RETURN,
        "code":"1",
        "function":s_display_game
    },
    {
        "text":INVENTORY,
        "code":"2",
        "function":s_inventory
    },

]

a_shop = [
    {
        "text":RETURN,
        "code":"1",
        "function":s_display_game
    },
    {
        "text":BUY,
        "code":"2",
        "function":s_buy
    },
    {
        "text":SELL,
        "code":"3",
        "function":s_sell
    },
]
a_quest = [
    {
        "text":RETURN,
        "code":"1",
        "function":s_display_game
    },
    {
        "text":CHOOSE_QUEST,
        "code":"2",
        "function":s_choose_quest
    },
]
a_boss = [
    {
        "text":RETURN,
        "code":"1",
        "function":s_display_game
    },
    {
        "text":END_GAME,
        "code":"2",
        "function":s_end_game
    },
]
