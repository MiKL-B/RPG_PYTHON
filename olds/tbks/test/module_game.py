import os
import sys
import time
import random
import json
import shutil
from rich.table import Table
from rich.console import Console


import module_player
import module_item
import module_data
import module_ui
import i18n.module_text as module_text
import module_menu


class Game:
    def __init__(self):
        self._hero = None


    def display_title(self):
        module_ui.clear_console()
        module_ui.print_message(module_text.TITLE_GAME)
        os.system(f"title The Barrel Kingdom")
        module_ui.print_separator()


    def main(self):
        self.display_title()
        if module_data.player_has_data():
            self.display_menu(module_menu.option_load, module_menu.function_load, self.main)
        else:
            self.display_menu(module_menu.option_new, module_menu.function_new, self.main)


    def display_menu(self,options,functions,function_return):
        table = Table()
        table.add_column("Menu")
        for index, item  in enumerate(options):
            if item != "":
                table.add_row(item[0] + " - " + item)
            else:
                table.add_row("")

        console = Console()
        console.print(table)
        module_ui.print_separator()
        choice = module_ui.input_command()

        for index, item in enumerate(options):
            if functions[index] != "":
                if choice == item[0].lower():
                    eval(functions[index])
        else:
            function_return()


    def new_player(self):
        self._hero = module_player.Player()
        self._hero.set_default_name()


    def load_player(self):
        self._hero = module_data.load()



    def game(self):
        module_ui.clear_console()
        module_ui.print_message(module_text.GAME)
        module_ui.print_separator()
        self._hero.print_position()
        module_ui.print_separator()
        self.display_menu(module_menu.option_game, module_menu.function_game, self.game)


    def display_menu_save(self):
        module_data.save(self._hero)
        module_ui.print_message(module_text.SAVED)
        print(f"{module_ui.get_date()} {self._hero._name}")
        module_ui.print_separator()
        self.display_menu(module_menu.option_return, module_menu.function_return, self.display_menu_save)


    def display_menu_options(self):
        module_ui.clear_console()
        module_ui.print_message(module_text.TITLE_OPTIONS)
        module_ui.print_separator()
        self.display_menu(module_menu.option_options, module_menu.function_options, self.display_menu_options)


    def display_menu_character(self):
        module_ui.clear_console()
        module_ui.print_message(module_text.CHARACTER)
        module_ui.print_separator()
        self._hero.info()
        module_ui.print_separator()
        self.display_menu(module_menu.option_character, module_menu.function_character, self.display_menu_character)


    def display_menu_inventory(self):
        module_ui.clear_console()
        module_ui.print_message(module_text.INVENTORY)
        module_ui.print_separator()
        self._hero.info_inventory()
        module_ui.print_separator()
        self.display_menu(module_menu.option_return, module_menu.function_return, self.display_menu_inventory)


    def quit(self):
        module_ui.clear_console()
        sys.exit()
