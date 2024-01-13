import inquirer
import tbk_ui
import tbk_text

class Player:
    def __init__(self,name="",job = None,loc_x=0, loc_y=0):
        self.name = name
        self.job = job
        self.loc_x = loc_x
        self.loc_y = loc_y

    def print_info(self):
        tbk_ui.print_msg("Name",self.name,"green")
        tbk_ui.print_msg("Job",self.job.name,"green")

    def print_position(self):
        tbk_ui.print_msg("X",self.loc_x,"green")
        tbk_ui.print_msg("Y",self.loc_y,"green")

    def set_name(self, question_name, answer_name):
        max_length_name = 10
        while True:
            length_name = len(answer_name["name"])
            if length_name <= max_length_name:
                break
            tbk_ui.print_msg("Name too long!","","red")
            answer_name = inquirer.prompt(question_name)

        if answer_name["name"] == "":
            answer_name["name"] = "Hero"

        self.name = answer_name["name"]
    
    def set_job(self,value):
        self.job = value

    def move(self,x,y):
        self.loc_x += x
        self.loc_y += y

    def move_north(self):
        """move north"""
        if self.loc_y > 0:
            self.move(0, -1)
        else:
            tbk_ui.print_msg(tbk_text.IMPOSSIBLE_DIRECTION,"","red")
            tbk_ui.wait()

    def move_west(self):
        """move west"""
        if self.loc_x > 0:
            self.move(-1, 0)
        else:
            tbk_ui.print_msg(tbk_text.IMPOSSIBLE_DIRECTION,"","red")
            tbk_ui.wait()

    def move_east(self):
        """move east"""
        if self.loc_x < 10:
            self.move(1, 0)
        else:
            tbk_ui.print_msg(tbk_text.IMPOSSIBLE_DIRECTION,"","red")
            tbk_ui.wait()

    def move_south(self):
        """move south"""
        if self.loc_y < 10:
            self.move(0, 1)
        else:
            tbk_ui.print_msg(tbk_text.IMPOSSIBLE_DIRECTION,"","red")
            tbk_ui.wait()

