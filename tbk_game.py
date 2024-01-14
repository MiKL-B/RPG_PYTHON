import sys

import tbk_menu as tbk_menu
import tbk_ui as tbk_ui
import tbk_text as tbk_text
import tbk_data
import tbk_player as tbk_player
import tbk_job as tbk_job
import tbk_item

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
        list_choices = [tbk_text.NORTH, tbk_text.WEST, tbk_text.EAST,tbk_text.SOUTH,tbk_text.CHARACTER,tbk_text.SAVE,tbk_text.QUIT]
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
            case tbk_text.CHARACTER:
                self.print_menu_player()
            case tbk_text.SAVE:
                self.save()
            case tbk_text.QUIT:
                self.quit()
        self.game()
    
    def print_menu_player(self):
        tbk_ui.clear()
        self.player.print_info()
        list_choices = [tbk_text.RETURN]
        menu_player = tbk_menu.Menu("player",tbk_menu.TYPE_LIST,list_choices)
        match menu_player.answer[menu_player.name]:
            case tbk_text.RETURN:
                self.game()

