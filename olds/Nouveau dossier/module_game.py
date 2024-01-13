import inquirer
import platform
import os
import time
import sys
import pickle
import module_player
import module_item
PATH = "save/SaveFile"

class Game:
    def __init__(self):
        self.player = None
    
    def __del__(self):
        pass

    # region main
    def main(self):
        self.clear()
        print("The Barrel Kingdom")
        print()
        self.display_menu_main()

    def display_menu_main(self):
        choices_main = ["New"]
        if self.has_save():
            choices_main.append("Load")
            choices_main.append("Delete")
        choices_main.append("Quit")
        question_main = [inquirer.List("main", message="Choose an option", choices=choices_main)]
        answer_main = inquirer.prompt(question_main)

        match answer_main["main"]:
            case "New":
                self.new()
            case "Load":
                self.load()
            case "Delete":
                self.delete()
            case "Quit":
                self.quit()

    def new(self):
        self.clear()
        self.create_player()
        self.display_introduction()
    
    def load(self):
        self.player = self.load_data()
        self.game()
    
    def save(self):
        self.save_data(self.player)
        print("Data saved!")
        self.wait()
        self.game()
    
    def delete(self):
        self.delete_data()
        print("Data deleted!")
        self.wait()
        self.main()

    def quit(self):
        self.clear()
        sys.exit()
    # endregion
        
    # region create player
    def create_player(self):
        self.player = module_player.Player("Player")
        self.player.inventory.append(module_item.potion)
        self.player.inventory.append(module_item.sword)
    # endregion
        
    # region game
    def display_introduction(self):
        self.clear()
        print("story introduction")
        print()
        self.wait()
        self.game()

    def game(self):
        self.clear()
        self.display_menu_game()

    def display_menu_game(self):
        choices_game = ["Character","Save","Quit"]
        question_game = [inquirer.List("game", message="Choose an option", choices=choices_game)]
        answer_game = inquirer.prompt(question_game)

        match answer_game["game"]:
            case "Character":
                self.display_menu_character()
            case "Save":
                self.save()
            case "Quit":
                self.quit()

    def display_menu_character(self):
        self.clear()
        self.player.refresh()
        print()

        choices_character = ["Inventory","Equipment","Return"]
        question_character = [inquirer.List("character", message="Choose an option", choices=choices_character)]
        answer_character = inquirer.prompt(question_character)

        match answer_character["character"]:
            case "Inventory":
                self.display_menu_inventory()
            case "Equipment":
                self.display_menu_equipment()
            case "Return":
                self.game()
    
    def display_menu_inventory(self):
        self.clear()
        print("Inventory:")
        self.player.refresh_inventory()
        print()
        choices_inventory = []
        for item in self.player.inventory:
            if isinstance(item, (module_item.Weapon)):
                choices_inventory.append("Equip")
        choices_inventory.append("Return")
        question_inventory = [inquirer.List("inventory", message="Choose an option", choices=choices_inventory)]
        answer_inventory = inquirer.prompt(question_inventory)

        match answer_inventory["inventory"]:
            case "Equip":
                self.display_menu_equipable()
            case "Return":
                self.display_menu_character()

    def display_menu_equipable(self):
        self.clear()
        print("Items to equip:")
        self.player.refresh_equipable_items()
        print()

        choices_equipable = []
        for item in self.player.inventory:
            if isinstance(item, (module_item.Weapon)):
                choices_equipable.append(item.name)
        choices_equipable.append("Return")

        question_equipable = [inquirer.List("equipable", message="Choose an option", choices=choices_equipable)]
        answer_equipable = inquirer.prompt(question_equipable)

        for item in self.player.inventory:
            if isinstance(item, (module_item.Weapon)):
                if answer_equipable["equipable"] == item.name:
                    self.player.equip(item)
                    print("Item equipped!")
                    self.wait()
                    self.display_menu_equipable()

        if answer_equipable["equipable"] == "Return":
            self.display_menu_inventory()

    def display_menu_equipment(self):
        self.clear()
        if self.player.weapon is not None:
            print(self.player.weapon.name)
        else:
            print("No equipment!")
        print()
        choices_equipment = []
        if self.player.weapon is not None:
            choices_equipment.append("Unequip")
        choices_equipment.append("Return")
        question_equipment = [inquirer.List("equipment", message="Choose an option", choices=choices_equipment)]
        answer_equipment = inquirer.prompt(question_equipment)

        match answer_equipment["equipment"]:
            case "Unequip":
                self.display_menu_unequipable()
            case "Return":
                self.display_menu_character()
    
    def display_menu_unequipable(self):
        self.clear()
        if self.player.weapon is not None:
            print(self.player.weapon.name)
        else:
            print("No item to unequip!")
        
        print()
        choices_unequipable = []
        if self.player.weapon is not None:
            choices_unequipable.append(self.player.weapon.name)
        choices_unequipable.append("Return")

        question_unequipable = [inquirer.List("unequipable", message="Choose an option", choices=choices_unequipable)]
        answer_unequipable = inquirer.prompt(question_unequipable)

        match answer_unequipable["unequipable"]:
            case self.player.weapon.name:
                    self.player.unequip(self.player.weapon)
                    print("Item unequipped!")
                    self.wait()
                    self.display_menu_unequipable()
            case "Return":
                self.display_menu_equipment()
    # endregion
        
    # region data
    def save_data(self, player) -> None:
        if not os.path.isdir("save"):
            os.mkdir("save")
        with open(PATH, "wb") as file_data:
            pickle.dump(player, file_data)

    def load_data(self):
        return pickle.load(open(PATH, "rb"))

    def delete_data(self) -> None:
        os.remove(PATH)

    def has_save(self) -> bool:
        return os.path.exists(PATH)
    # endregion

    # region ui
    def clear(self):
        os.system("cls")
        if platform in {"linux","darwin"}:
            os.system('clear')
    
    def wait(self):
        time.sleep(2)
    # endregion

