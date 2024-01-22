import sys

import tbk_menu
import tbk_ui
import tbk_text
import tbk_data
import tbk_player
import tbk_job
import tbk_item
import tbk_worldmap

class Game:
    def __init__(self):
        self.player = None

    def __del__(self):
        pass

    # region main
    def main(self):
        tbk_ui.print_title(tbk_text.GAME_TITLE)

        list_choices = [tbk_text.NEW]
        if tbk_data.has_save():
            list_choices.append(tbk_text.LOAD)
            list_choices.append(tbk_text.DELETE)
        list_choices.append(tbk_text.QUIT)

        menu_main = tbk_menu.Menu("main", tbk_menu.TYPE_LIST, list_choices)
        match menu_main.answer[menu_main.name]:
            case tbk_text.NEW:
                self.new()
            case tbk_text.LOAD:
                self.load()
            case tbk_text.DELETE:
                self.delete()
            case tbk_text.QUIT:
                self.quit()

    def new(self):
        tbk_ui.clear()
        self.create_player()
        self.print_introduction()

    def load(self):
        self.player = tbk_data.load_data()
        self.game()

    def save(self):
        tbk_data.save_data(self.player)
        tbk_ui.print_msg(tbk_text.DATA_SAVED,"","green")
        tbk_ui.wait()
        self.game()

    def delete(self):
        tbk_data.delete_data()
        tbk_ui.print_msg(tbk_text.DATA_DELETED, "", "green")
        tbk_ui.wait()
        self.main()

    def quit(self):
        tbk_ui.clear()
        sys.exit()
    # endregion

    def create_player(self):
        self.player = tbk_player.Player()

        # choose name
        menu_player_name = tbk_menu.Menu("name", tbk_menu.TYPE_TEXT)
        self.player.set_name(menu_player_name.question,menu_player_name.answer)

        # choose job
        list_choices = [tbk_job.warrior.name,tbk_job.wizard.name,tbk_job.rogue.name]
        menu_player_job = tbk_menu.Menu("job", tbk_menu.TYPE_LIST, list_choices)
        match menu_player_job.answer[menu_player_job.name]:
            case tbk_job.warrior.name:
                job = tbk_job.warrior
            case tbk_job.wizard.name:
                job = tbk_job.wizard
            case tbk_job.rogue.name:
                job = tbk_job.rogue
        
        self.player.set_job(job)

    def print_introduction(self):
        tbk_ui.clear()
        tbk_ui.print_msg(tbk_text.STORY)
        menu_introduction = tbk_menu.Menu("introduction", tbk_menu.TYPE_LIST, [tbk_text.CONTINUE])
        if menu_introduction.answer[menu_introduction.name] == tbk_text.CONTINUE:
            self.game()

    def game(self):
        tbk_ui.clear()
        self.player.print_position()
        print()
        list_choices = [tbk_text.NORTH,
                        tbk_text.WEST,
                        tbk_text.EAST,
                        tbk_text.SOUTH,
                        tbk_text.WORLD_MAP]
        
        if self.player.is_in_town():
            list_choices.append(tbk_text.TOWN)
        else:
            list_choices.append(tbk_text.COMBAT)
        list_choices.append(tbk_text.CHARACTER)
        list_choices.append(tbk_text.SAVE)
        list_choices.append(tbk_text.QUIT)               
                        
        menu_game = tbk_menu.Menu("game", tbk_menu.TYPE_LIST, list_choices)
        match menu_game.answer[menu_game.name]:
            case tbk_text.NORTH:
                self.player.move_north()
            case tbk_text.WEST:
                self.player.move_west()
            case tbk_text.EAST:
                self.player.move_east()
            case tbk_text.SOUTH:
                self.player.move_south()
            case tbk_text.WORLD_MAP:
                self.print_menu_world_map()
            case tbk_text.CHARACTER:
                self.print_menu_player()
            case tbk_text.TOWN:
                self.print_menu_town()
            case tbk_text.COMBAT:
                self.print_menu_combat()
            case tbk_text.SAVE:
                self.save()
            case tbk_text.QUIT:
                self.quit()
        self.game()
    
    # region print menu game
    def print_menu_world_map(self):
        tbk_ui.clear()
        tbk_worldmap.display(self.player.world_map_y, self.player.world_map_x, self.player.loc_y, self.player.loc_x)
        print()
        list_choices = [tbk_text.RETURN]
        menu_player = tbk_menu.Menu("player",tbk_menu.TYPE_LIST,list_choices)
        match menu_player.answer[menu_player.name]:
            case tbk_text.RETURN:
                self.game()

    def print_menu_player(self):
        tbk_ui.clear()
        self.player.print_info()
        self.player.print_gold()
        print()
        list_choices = [tbk_text.INVENTORY,
                        tbk_text.EQUIPMENT,
                        tbk_text.QUESTS,
                        tbk_text.SKILLS,
                        tbk_text.BLACKSMITHING,
                        tbk_text.BESTIARY,
                        tbk_text.FISHING_DIARY,
                        tbk_text.RETURN]
        menu_player = tbk_menu.Menu("player",tbk_menu.TYPE_LIST,list_choices)
        match menu_player.answer[menu_player.name]:
            case tbk_text.QUESTS:
                self.print_menu_quests()
            case tbk_text.EQUIPMENT:
                self.print_menu_equipment()
            case tbk_text.INVENTORY:
                self.print_menu_inventory()
            case tbk_text.SKILLS:
                self.print_menu_skills()
            case tbk_text.BESTIARY:
                self.print_menu_bestiary()
            case tbk_text.FISHING_DIARY:
                self.print_menu_fishing_diary()
            case tbk_text.BLACKSMITHING:
                self.print_menu_blacksmithing()
            case tbk_text.RETURN:
                self.game()

    def print_menu_town(self): # TODO
        # tavern
        #   - bounty boards
        # job master
        #
        pass
    
    def print_menu_tavern(self): # TODO
        pass

    def print_menu_job_master(self): # TODO
        pass

    def print_menu_combat(self): # TODO
        pass

    def print_menu_quests(self): # TODO
        pass

    def print_menu_equipment(self):
        tbk_ui.clear()
        tbk_ui.print_title(tbk_text.EQUIPMENT)
        self.player.print_equipment()
        print()
        list_choices = []
        if len(self.player.get_list_equipment()) > 0:
            list_choices.append(tbk_text.UNEQUIP_ITEM)
        list_choices.append(tbk_text.RETURN)
        menu_player = tbk_menu.Menu("player",tbk_menu.TYPE_LIST,list_choices)
        match menu_player.answer[menu_player.name]:
            case tbk_text.UNEQUIP_ITEM:
                self.print_menu_unequip_item()
            case tbk_text.RETURN:
                self.print_menu_player()
    
    def print_menu_unequip_item(self):
        tbk_ui.clear()
        self.player.print_equipment()
        print()

        list_choices = []
        for item in self.player.get_list_equipment():
            list_choices.append(item.name) 
        list_choices.append(tbk_text.RETURN)

        menu_player = tbk_menu.Menu("player",tbk_menu.TYPE_LIST,list_choices)
        
        for item in self.player.get_list_equipment():
            if menu_player.answer[menu_player.name] == item.name:
                self.player.unequip_item(item)
                self.print_menu_unequip_item()
        if menu_player.answer[menu_player.name] == tbk_text.RETURN:
            self.print_menu_equipment()

    def print_menu_inventory(self):
        tbk_ui.clear()
        tbk_ui.print_title(tbk_text.INVENTORY)
        self.player.print_inventory()
        print()
        list_choices = []
        if len(self.player.get_list_consumable()) > 0:
            list_choices.append(tbk_text.USE_ITEM)
        
        if len(self.player.get_list_equipable()) > 0:
            list_choices.append(tbk_text.EQUIP_ITEM)

        list_choices.append(tbk_text.RETURN)

        menu_player = tbk_menu.Menu("player",tbk_menu.TYPE_LIST,list_choices)
        match menu_player.answer[menu_player.name]:
            case tbk_text.USE_ITEM:
                self.print_menu_use_item()
            case tbk_text.EQUIP_ITEM:
                self.print_menu_equip_item()
            case tbk_text.RETURN:
                self.print_menu_player()

    def print_menu_use_item(self):
        tbk_ui.clear()
        self.player.print_consumable()
        print()

        list_choices = []
        for item in self.player.get_list_consumable():
            list_choices.append(item.name) 
        list_choices.append(tbk_text.RETURN)

        menu_player = tbk_menu.Menu("player",tbk_menu.TYPE_LIST,list_choices)
        
        for item in self.player.get_list_consumable():
            if menu_player.answer[menu_player.name] == item.name:
                self.player.use_item(item)
                self.print_menu_use_item()
        if menu_player.answer[menu_player.name] == tbk_text.RETURN:
            self.print_menu_inventory()

    def print_menu_equip_item(self):
        tbk_ui.clear()
        self.player.print_equipable()
        print()

        list_choices = []
        for item in self.player.get_list_equipable():
            list_choices.append(item.name)
        list_choices.append(tbk_text.RETURN)

        menu_player = tbk_menu.Menu("player",tbk_menu.TYPE_LIST,list_choices)

        for item in self.player.get_list_equipable():
            if menu_player.answer[menu_player.name] == item.name:
                self.player.equip_item(item)
                self.print_menu_equip_item()
        if menu_player.answer[menu_player.name] == tbk_text.RETURN:
            self.print_menu_inventory()  

    def print_menu_skills(self): # TODO
        pass

    def print_menu_bestiary(self): # TODO
        pass

    def print_menu_fishing_diary(self): # TODO
        pass
    
    def print_menu_blacksmithing(self): # TODO
        pass
    # endregion