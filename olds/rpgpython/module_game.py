"""module game"""
import os
import sys
import pickle
import inquirer
import module_text
import module_ui
import module_hero
import module_job
import module_item
import module_player
import module_map

class Game:
    """main class"""

    def __init__(self):
        self.player = None

    def __del__(self):
        pass

    # region menu
    def main(self):
        """the main menu"""
        module_ui.clear()
        print(module_ui.color(module_text.GAME_TITLE, 'yellow'))
        module_ui.separator()

        list_choices = [module_text.NEW]
        if self.has_save():
            list_choices.append(module_text.LOAD)
            list_choices.append(module_text.DELETE)
        list_choices.append(module_text.OPTIONS)
        list_choices.append(module_text.QUIT)

        question_main = [
            inquirer.List(module_text.MAIN,
                          message=module_text.CHOOSE_OPTION,
                          choices=list_choices),
        ]
        answer_main = inquirer.prompt(question_main)

        match answer_main[module_text.MAIN]:
            case module_text.NEW:
                self.new_game()
            case module_text.LOAD:
                self.load_game()
            case module_text.DELETE:
                self.delete_game()
            case module_text.OPTIONS:
                self.option_game()
            case module_text.QUIT:
                self.quit_game()

    def new_game(self):
        """launch a new game"""
        module_ui.clear()
        self.create_heroes()
        self.introduction()

    def load_game(self):
        """load the game"""
        self.player = self.load_data()
        self.launch_adventure()

    def save_game(self):
        """save the game"""
        self.save_data(self.player)
        print(module_ui.color(module_text.DATA_SAVED, 'green'))
        module_ui.wait()
        self.launch_adventure()

    def delete_game(self):
        """delete the game"""
        self.delete_data()
        print(module_ui.color(module_text.DATA_DELETED, 'green'))
        module_ui.wait()
        self.main()

    def option_game(self):
        """display option game"""
        module_ui.clear()
        print("option game")
        module_ui.separator()
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=[module_text.CHANGE_LANGUAGE,
                                   module_text.ABOUT,
                                   module_text.RETURN]),
        ]
        answer = inquirer.prompt(question)
        match answer[module_text.ADVENTURE]:
            case module_text.CHANGE_LANGUAGE:
                self.change_locale_language()
            case module_text.ABOUT:
                self.about_game()
            case module_text.RETURN:
                self.main()

    def change_locale_language(self):
        """change locale language"""
        module_ui.clear()
        print("change language")
        module_ui.wait()
        self.option_game()

    def about_game(self):
        """about game"""
        module_ui.clear()
        print("about copyright, game rules...")
        module_ui.wait()
        self.option_game()

    def quit_game(self):
        """quit the game"""
        module_ui.clear()
        sys.exit()
    # endregion

    # region data
    def save_data(self, player) -> None:
        """save the player in the save/SaveFile"""
        if not os.path.isdir("save"):
            os.mkdir("save")
        with open(module_text.PATH, "wb") as file_data:
            pickle.dump(player, file_data)

    def load_data(self):
        """load the hero from the file"""
        return pickle.load(open(module_text.PATH, "rb"))

    def delete_data(self) -> None:
        """delete the file"""
        os.remove(module_text.PATH)

    def has_save(self) -> bool:
        """check if a save file exists"""
        return os.path.exists(module_text.PATH)
    # endregion

    # region create hero
    def create_heroes(self):
        """create the hero"""
        # create player
        self.player = module_player.Player()

        hero1 = module_hero.Hero()
        hero2 = module_hero.Hero()
        hero3 = module_hero.Hero()
        list_hero = [hero1, hero2, hero3]
        print("Choose name and job for your heroes")
        module_ui.separator()

        # create heroes
        for index, hero in enumerate(list_hero):
            # choose name
            question_name = [inquirer.Text(
                module_text.NAME, message=module_text.CHOOSE_NAME + " for the hero " + str(index + 1))]
            answer_name = inquirer.prompt(question_name)
            hero.name = self.validate_name(question_name, answer_name, index)

            # choose job
            question_job = [inquirer.List(
                module_text.JOB, message=module_text.CHOOSE_JOB + " for the hero " + str(index + 1), choices=[
                    module_job.WARRIOR.name,
                    module_job.ROGUE.name,
                    module_job.WIZARD.name])]
            answer_job = inquirer.prompt(question_job)
            hero.set_job(answer_job[module_text.JOB])
            # define other properties

            self.player.heroes.append(hero)

    def validate_name(self, question_name, answer_name, index):
        """ return valid name"""
        max_length_name = 10
        while True:
            length_name = len(answer_name[module_text.NAME])
            if length_name <= max_length_name:
                break
            print(f"{module_ui.color(module_text.NAME_TOO_LONG,'red')}")
            answer_name = inquirer.prompt(question_name)

        if answer_name[module_text.NAME] == "":
            answer_name[module_text.NAME] = module_text.HERO + str(index + 1)

        return answer_name[module_text.NAME]
    # endregion

    # region launch game
    def introduction(self):
        """display an introduction message"""
        module_ui.clear()
        print("story")
        module_ui.separator()
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=[module_text.CONTINUE]),
        ]
        answer = inquirer.prompt(question)
        if answer[module_text.ADVENTURE] == module_text.CONTINUE:
            self.launch_adventure()

    def launch_adventure(self):
        """launch the aventure"""
        module_ui.clear()
        print(module_ui.color(module_text.GAME_TITLE, 'yellow'))
        module_map.display(self.player.world_map_y, self.player.world_map_x,
                           self.player.location_y, self.player.location_x)
        module_ui.separator()
        self.player.refresh_position()
        module_ui.separator()
        self.display_menu_adventure()
        self.launch_adventure()

    def display_menu_adventure(self):
        """display menu adventure"""
        choices_adventure = [module_text.GO_NORTH,
                             module_text.GO_WEST,
                             module_text.GO_EAST,
                             module_text.GO_SOUTH,
                             module_text.CHARACTER]

        if self.player.is_in_town():
            choices_adventure.append(module_text.TOWN)
        
        choices_adventure.append(module_text.SAVE)
        choices_adventure.append(module_text.QUIT)

        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=choices_adventure),
        ]
        answer = inquirer.prompt(question)
        match answer[module_text.ADVENTURE]:
            case module_text.GO_NORTH:
                self.player.move_north()
            case module_text.GO_WEST:
                self.player.move_west()
            case module_text.GO_EAST:
                self.player.move_east()
            case module_text.GO_SOUTH:
                self.player.move_south()
            case module_text.CHARACTER:
                self.display_character()
            case module_text.TOWN:
                self.display_menu_town()
            case module_text.SAVE:
                self.save_game()
            case module_text.QUIT:
                self.quit_game()  
    # endregion

    # region character
    def display_character(self):
        """display character"""
        module_ui.clear()
        self.player.refresh()
        module_ui.separator()
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=[module_text.EQUIPMENT,
                                   module_text.INVENTORY,
                                   module_text.QUESTS,
                                   module_text.BESTIARY,
                                   module_text.FISHING_DIARY,
                                   module_text.SKILLS,
                                   module_text.RETURN]),
        ]
        answer = inquirer.prompt(question)
        match answer[module_text.ADVENTURE]:
            case module_text.EQUIPMENT:
                self.display_menu_equipment()
            case module_text.INVENTORY:
                self.display_menu_inventory()
            case module_text.QUESTS:
                self.display_menu_quests()
            case module_text.BESTIARY:
                self.display_menu_bestiary()
            case module_text.FISHING_DIARY:
                self.display_menu_fishing_diary()
            case module_text.SKILLS:
                self.display_menu_skills()
            case module_text.RETURN:
                self.launch_adventure()

    def display_menu_equipment(self):
        """display equipment character"""
        module_ui.clear()
        print("equipment")
        module_ui.separator()
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=[module_text.UNEQUIP,
                                   module_text.RETURN]),
        ]
        answer = inquirer.prompt(question)
        match answer[module_text.ADVENTURE]:
            case module_text.UNEQUIP:
                self.display_menu_unequip()
            case module_text.RETURN:
                self.display_character()

    def display_menu_unequip(self):
        """unequip an item"""
        pass

    def display_menu_inventory(self):
        """display menu inventory"""
        module_ui.clear()
        self.player.refresh_inventory()
        module_ui.separator()
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=[module_text.USE,
                                   module_text.EQUIP,
                                   module_text.RETURN]),
        ]
        answer = inquirer.prompt(question)
        match answer[module_text.ADVENTURE]:
            case module_text.USE:
                self.display_menu_use_item()
            case module_text.EQUIP:
                self.display_menu_equip()
            case module_text.RETURN:
                self.display_character()

    def display_menu_use_item(self):
        """use an item in the inventory"""
        # list of item like consumable

    def display_menu_equip(self):
        """equip an item in the inventory"""
        # list of item like weapon or armor
        module_ui.clear()
        self.player.refresh_equipable_items()
        module_ui.separator()

        list_choices = []
        for item in self.player.inventory:
            if isinstance(item, (module_item.Weapon,module_item.Armor)):
                list_choices.append(item.name)
        list_choices.append(module_text.RETURN)

        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=list_choices),
        ]
        answer = inquirer.prompt(question)
        for item in self.player.inventory:
            if isinstance(item, (module_item.Weapon,module_item.Armor)):
                if answer[module_text.ADVENTURE] == item.name:
                    print(f"equip: {item.name}")
                    module_ui.wait()
                    self.display_menu_equip()
        if answer[module_text.ADVENTURE] == module_text.RETURN:
            self.display_menu_inventory()

    def display_menu_quests(self):
        """display quests character"""
        module_ui.clear()
        print("quests")
        # display list of main quests
        # display bounty list
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=[module_text.GIVE_UP_BOUNTY,
                                   module_text.RETURN]),
        ]
        answer = inquirer.prompt(question)
        match answer[module_text.ADVENTURE]:
            case module_text.GIVE_UP_BOUNTY:
                self.give_up_bounty()
            case module_text.RETURN:
                self.display_character()

    def give_up_bounty(self):
        """give up a secondary quest"""
        # display bounty list
        # list choices with bounty to give up

    def display_menu_bestiary(self):
        """display bestiary character"""
        module_ui.clear()
        print("bestiary")
        # display list of monsters which are defeated by the hero
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=[module_text.RETURN]),
        ]
        answer = inquirer.prompt(question)
        if answer[module_text.ADVENTURE] == module_text.RETURN:
            self.display_character()

    def display_menu_fishing_diary(self):
        """display fishing diary character"""
        module_ui.clear()
        print("fishing diary")
        # display list of fishes which are caught by the hero
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=[module_text.RETURN]),
        ]
        answer = inquirer.prompt(question)
        if answer[module_text.ADVENTURE] == module_text.RETURN:
            self.display_character()

    def display_menu_skills(self):
        """display skills character"""
        module_ui.clear()
        print("skills")
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=[module_text.RETURN]),
        ]
        answer = inquirer.prompt(question)
        if answer[module_text.ADVENTURE] == module_text.RETURN:
            self.display_character()
    # endregion

    # region town
    def display_menu_town(self):
        """display town"""
        module_ui.clear()
        print("town name")
        module_ui.separator()
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=[module_text.SHOP,
                                   module_text.TAVERN,
                                   module_text.RETURN]),
        ]
        answer = inquirer.prompt(question)
        match answer[module_text.ADVENTURE]:
            case module_text.SHOP:
                self.display_shop()
            case module_text.TAVERN:
                self.display_tavern()
            case module_text.RETURN:
                self.launch_adventure()

    def display_shop(self):
        """display shop"""
        module_ui.clear()
        print("shop name")
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=[module_text.BUY,
                                   module_text.SELL,
                                   module_text.RETURN]),
        ]
        answer = inquirer.prompt(question)
        match answer[module_text.ADVENTURE]:
            case module_text.BUY:
                self.display_buy_menu()
            case module_text.SELL:
                self.display_sell_menu()
            case module_text.RETURN:
                self.display_menu_town()

    def display_buy_menu(self):
        """buy menu"""
        module_ui.clear()
        # display list of item shop
        module_item.refresh_shop()
        self.player.refresh_gold()
        module_ui.separator()

        list_choices = []
        for item in module_item.shop:
            list_choices.append(item.name)
        list_choices.append(module_text.RETURN)

        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_ITEM_TO_BY,
                          choices=list_choices),
        ]
        answer = inquirer.prompt(question)

        for item in module_item.shop:
            if answer[module_text.ADVENTURE] == item.name:
                self.player.buy_item(item)
                module_ui.wait()
                self.display_buy_menu()
        if answer[module_text.ADVENTURE] == module_text.RETURN:
            self.display_shop()

    def display_sell_menu(self):
        """sell menu"""
        module_ui.clear()
        # display list of inventory
        self.player.refresh_inventory()
        self.player.refresh_gold()
        module_ui.separator()

        list_choices = []
        if len(self.player.inventory) > 0:
            for item in self.player.get_inventory():
                list_choices.append(item.name)
        list_choices.append(module_text.RETURN)

        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_ITEM_TO_SELL,
                          choices=list_choices),
        ]
        answer = inquirer.prompt(question)
        for item in self.player.inventory:
            if answer[module_text.ADVENTURE] == item.name:
                self.player.sell_item(item)
                module_ui.wait()
                self.display_sell_menu()

        if answer[module_text.ADVENTURE] == module_text.RETURN:
            self.display_shop()

    def display_tavern(self):
        """display tavern"""
        module_ui.clear()
        print("tavern name")
        module_ui.separator()
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=[module_text.BOUNTY_BOARDS,
                                   module_text.JOB_MASTER,
                                   module_text.RETURN]),
        ]
        answer = inquirer.prompt(question)
        match answer[module_text.ADVENTURE]:
            case module_text.BOUNTY_BOARDS:
                self.display_bounty_boards()
            case module_text.JOB_MASTER:
                self.display_job_master()
            case module_text.RETURN:
                self.display_menu_town()

    def display_bounty_boards(self):
        """display bounty boards"""
        module_ui.clear()
        print("list bounty here")
        # if list bounty == 0
        # empty bounty list

        list_choices = []
        # for item in bountylist:
        # list_choices.append(item)
        list_choices.append(module_text.RETURN)
        module_ui.separator()
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=list_choices),
        ]
        answer = inquirer.prompt(question)
        # for item in bountylist:
        # if answer[module_text.ADVENTURE] == item.name
        # self.hero.pickup_bounty(item)
        # module_ui.wait
        # self.display_bounty_boards()
        if answer[module_text.ADVENTURE] == module_text.RETURN:
            self.display_tavern()

    def display_job_master(self):
        """display job master"""
        module_ui.clear()
        print("skill to learn here")
        print("maitre de classe enac: etrange nain a capuche")
        module_ui.separator()
        question = [
            inquirer.List(module_text.ADVENTURE,
                          message=module_text.CHOOSE_OPTION,
                          choices=[module_text.RETURN]),
        ]
        answer = inquirer.prompt(question)
        if answer[module_text.ADVENTURE] == module_text.RETURN:
            self.display_tavern()
    # endregion
