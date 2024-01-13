"""tbk_menu"""
import inquirer

TYPE_LIST = "list"
TYPE_TEXT = "text"
TYPE_CHECKBOX = "checkbox"

class Menu:
    """class menu"""
    def __init__(self, name="", category="", choices="", message="", question="", answer=""):
        self.name = name
        self.category = category
        self.choices = choices
        self.message = message
        self.question = question
        self.answer = answer

        match self.category:
            case "list":
                self.message = "Choose an option"
                self.question = [inquirer.List(
                    self.name, self.message, self.choices)]
            case "text":
                self.message = "Enter a value"
                self.question = [inquirer.Text(self.name, self.message)]
            case "checkbox":
                self.message = "Choose one or many checkbox"
                self.question = [inquirer.Checkbox(
                    self.name, self.message, self.choices)]

        self.answer = inquirer.prompt(self.question)
        