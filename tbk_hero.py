import tbk_ui
import tbk_level
import inquirer

class Hero:
    def __init__(self):
        self.name = name
        self.job = job
        self.health = health
        self.max_health = max_health
        self.state = state
        if equipment == None:
            equipment =  []
        self.equipment = equipment
        self.level = level
        self.experience = experience

    # region refresh
    def print_info(self):
        tbk_ui.print_msg("Name",self.name,"green")
        tbk_ui.print_msg("Job",self.job.name,"green")
        tbk_ui.print_msg("Level",self.level,"green")
        self.print_experience()
        tbk_ui.print_msg("Health",str(self.health) + " / " + str(self.max_health), "green")
    # endregion
        
    def print_equipment(self):
        if len(self.equipment) > 0:
            for item in self.equipment:
                tbk_ui.print_msg("Item",item.name,"green")
        else:
            print("Equipment empty!")
    
    def print_experience(self):
        max_experience = tbk_level.levels[self.level-1]['max_experience']
        tbk_ui.print_msg("Exp", str(self.experience) + " / " + str(max_experience),"green")

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