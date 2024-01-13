import sys
import tbk_menu
import tbk_ui
import tbk_text
import tbk_data
import tbk_player


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
        tbk_ui.clear()
        self.player = tbk_data.load_data()
        tbk_ui.print_msg(tbk_text.DATA_LOADED, "", "green")
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

    def print_introduction(self):
        tbk_ui.print_msg(tbk_text.STORY)
        print(self.player)

    def game(self):
        pass
