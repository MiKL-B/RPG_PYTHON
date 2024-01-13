"""Docstring d'une ligne décrivant brièvement ce que fait le programme.

Usage:
======
    python nom_de_ce_super_script.py argument1 argument2

    argument1: un entier signifiant un truc
    argument2: une chaîne de caractères décrivant un bidule
"""
import pickle
import sys
import os
import random
from rich.console import Console

import module_ui
import module_menu
import module_text

import Player
from Shop import my_shop
from Monster import random_monster
from Location import *
from Quests import *


class Game:
	def __init__(self):
		self._hero = None
		self._data = None
		self._monster = None

	def __del__(self):
		pass

	def main(self):
		module_ui.clear_console()
		module_ui.print_message(module_text.TITLE_GAME)
		os.system("title The Barrel Kingdom")

		if self.is_any_data():
			self.display_menu(module_menu.a_main_data, self.main)
		else:
			self.display_menu(module_menu.a_main, self.main)


	def display_menu(self, menu, function_return):
		module_ui.print_separator()
		for index, item in enumerate(menu):
			print(item['code'], item['text'])

		module_ui.print_separator()

		choice = module_ui.input_command()
		for index, item in enumerate(menu):
			if choice == item['code'].lower():
				if item['function'] != "":
					eval(item['function'])
		else:
			function_return()


	def display_help_menu(self):
		module_ui.clear_console()
		module_ui.print_message(module_text.WEBSITE)
		self.display_menu(module_menu.a_return_main, self.display_help_menu)


	def new_player(self):
		c_Player = Player.Player()
		return c_Player


	def define_new_player(self):
		self._hero = self.new_player()
		self._hero.set_default_value()


	def load_game(self):
		if self.is_any_data():
			self._data = pickle.load(open("save/SaveFile", "rb"))
			self._hero = self._data
		return self._data


	def save_game(self):
		pickle.dump(self._hero, open("save/SaveFile","wb"))
		module_ui.clear_console()
		module_ui.print_message(module_text.SAVED)
		self._hero.print_info()
		self._hero.display_inventory()
		self._hero.sheet_quests()
		self.display_menu(module_menu.a_return_game, self.save_game)


	def delete_game(self):
		module_ui.clear_console()
		module_ui.print_message(module_text.DELETE_CONFIRM)
		self.display_menu(module_menu.a_confirm_delete, self.delete_game)
		

	def delete(self):
		os.remove("save/SaveFile")
		module_ui.clear_console()
		module_ui.print_message(module_text.DATA_DELETED)
		module_ui.wait(2)
		self.main()


	def is_any_data(self):
		s_path = "save/SaveFile"
		b_is_file_exist = os.path.exists(s_path)
		return b_is_file_exist


	def quit(self):
		module_ui.clear_console()
		sys.exit()
		

	def intro_story(self):
		module_ui.clear_console()
		module_ui.print_message(module_text.STORY)
		self.display_menu(module_menu.a_next, self.intro_story)


	def display_game(self):
		module_ui.clear_console()
		self._hero.display_position()
		display_world_map(self._hero._positionY,self._hero._positionX)
		module_ui.print_separator()
		self.display_menu(module_menu.a_game, self.display_game)


	def display_menu_options(self):
		module_ui.clear_console()
		module_ui.print_message(module_text.SETTINGS)
		self.display_menu(module_menu.a_options, self.display_menu_options)


	def sheet_hero(self):
		module_ui.clear_console()
		self._hero.print_info()
		self.display_menu(module_menu.a_sheet_hero, self.sheet_hero)


	def display_menu_inventory(self):
		module_ui.clear_console()
		print("1 Return")
		if not self._hero.has_inventory_empty():
			print("2 Equip")
			print("3 Unequip")
			print("4 Use an object")
			module_ui.print_separator()
		self._hero.display_inventory()
		choice = module_ui.input_command()
		if choice == "1":
			self.sheet_hero()
		elif choice == "4":
			if not self._hero.has_inventory_empty():
				self.choose_item_to_use()
			else:
				self.display_menu_inventory()
		else:
			self.display_menu_inventory()


	def display_quests_character(self):
		module_ui.clear_console()
		self._hero.sheet_quests()
		self.display_menu(module_menu.SHEET_QUESTS, self.display_quests_character)


	def choose_item_to_use(self):
		module_ui.clear_console()
		self._hero.display_inventory()
		module_ui.print_separator()
		print("1 Return")
		print("which one to use")

		choice = module_ui.input_command()
		for index, item in enumerate(self._hero._inventory):
			if choice == str(item._index):
				self._hero.use_item(item)
				self.display_menu_inventory()
			elif choice == "1":
				self.display_menu_inventory()
		else:
			self.choose_item_to_use()


	def display_menu_shop(self):
		module_ui.clear_console()
		module_ui.print_separator()
		my_shop.display_shop_info()
		module_ui.print_separator()

		self._hero.display_inventory()
		self._hero.display_gold()

		self.display_menu(module_menu.a_shop, self.display_menu_shop)


	def choose_item_to_buy(self):
		module_ui.clear_console()
		my_shop.display_shop_info()
		module_ui.print_separator()
		print("1 Return")
		print("which one to buy")
		
		choice = module_ui.input_command()
		for index, item in enumerate(my_shop._stock_item):
			if choice == str(item._index):
				self._hero.buy_item(item)
				self.display_menu_shop()
			elif choice == "1":
				self.display_menu_shop()
		else:
			self.choose_item_to_buy()


	def choose_item_to_sell(self):
		if self._hero.has_inventory_empty():
			print("vous n'avez rien a vendre")
			module_ui.wait(2)
			self.display_menu_shop()
		else:
			module_ui.clear_console()
			self._hero.display_inventory()
			module_ui.print_separator()
			print("1 Return")
			print("which one to sell")
			
			choice = module_ui.input_command()
			for index, item in enumerate(self._hero._inventory):
				if choice == str(item._index):
					self._hero.sell_item(item)
					self.display_menu_shop()
				elif choice == "1":
					self.display_menu_shop()
			else:
				self.choose_item_to_sell()


	def display_menu_combat(self):
		module_ui.clear_console()
		print("1 Leave")
		print("2 Take the fight")

		module_ui.print_separator()
		
		self._monster.display_info_combat()
		module_ui.print_separator()
		self._hero.display_info_combat()

		choice = module_ui.input_command()
		if choice == "1":
			if self._hero.is_the_fastest(self._monster):
				self.display_game() # the player can leave the combat
			else:
				print("you can not leave, you must take the fight")
				module_ui.wait(2)
				self.combat()
		elif choice == "2":
			self.combat()
		else:
			self.display_menu_combat()


	def combat(self):
		module_ui.clear_console()
		print("COMBAT:")
		print("1 ATK")
		print("2 use a potion")

		module_ui.print_separator()
		self._monster.display_info_combat()
		module_ui.print_separator()
		self._hero.display_info_combat()
		
		choice = module_ui.input_command()
		
		if choice == "1":
			if self._hero.is_dead(): # replace by is_alive(): -> return self._health > 0
				print("you loose")
				module_ui.wait(2)
				self.main()
			else:
				self._hero.attack_target(self._monster)

			if self._monster.is_dead():
				self.display_menu_reward()
				
			else:
				self._monster.attack_target(self._hero)
			self.combat()
		else:
			self.combat()


	def display_menu_reward(self):
		module_ui.clear_console()
		print("1 continue")
		module_ui.print_separator()
		exp = 10
		item = self._monster._loot
		self._hero.get_reward(exp,item)
		module_ui.print_separator()
		print("you have defeated the monster")
		print(f"you have earned {exp} experience and a {item._name}")
		choice = module_ui.input_command()
		if choice == "1":
			self.display_game()
		else:
			self.display_menu_reward()


	def random_combat(self):
		if not is_player_in_town(self._hero._positionY,self._hero._positionX):
			rd = random.randint(1,5)
			if rd == 4:
				self._monster = random_monster()
				self.display_menu_combat()


	def display_menu_quest(self):
		module_ui.clear_console()
		display_quest_info()
		self.display_menu(module_menu.a_quest, self.display_menu_quest)


	def choose_quest_to_accept(self):
		module_ui.clear_console()
		print("1 Return")
		display_quest_info()
		print("which one to accept")
		choice = module_ui.input_command()
		for index, item in enumerate(list_quest):
			if choice == str(item._index):
				self._hero._quests.append(item)
				print("quest accepted")
				module_ui.wait(2)
				self.display_menu_quest()
			elif choice == "1":
				self.display_menu_quest()
		else:
			self.choose_quest_to_accept()


	def display_menu_boss(self):
		module_ui.clear_console()
		module_ui.print_message(module_text.DRAGON_COMBAT)
		self.display_menu(module_menu.a_boss, self.display_menu_boss)


	def end_game(self):
		module_ui.clear_console()
		module_ui.print_message(module_text.END_GAME)
		module_ui.wait(5)
		self.main()
