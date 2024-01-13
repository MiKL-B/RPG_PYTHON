"""class Hero"""
import module_ui
from module_character import Character


class Hero(Character):
    """class Hero"""

    def __init__(self, index=-1, name="", level=1,
                 health=10, max_health=10, attack=0,
                 defense=0, magic=0, resource=100, max_resource=100,
                 x=0, y=0, experience=0, max_experience=0, job="",weapon=None):
        Character.__init__(self, index, name, level, health,
                           max_health, attack, defense, magic,
                           resource, max_resource, x, y)
        self.experience = experience
        self.max_experience = max_experience
        self.job = job
        if weapon is None:
            weapon = {}
        self.weapon = weapon
        # equipment
        # if skills is None:
        # skills = []
        # self.skills = skills

    def refresh(self):
        """refresh info"""
        print(f"Name: {module_ui.color(self.name,'green')}")
        print(f"Level: {module_ui.color(self.level,'green')}")
        print(f"Class: {module_ui.color(self.job,'green')}")
        module_ui.separator()
        module_ui.display_resource_bar(
            "Health:", self.health, self.max_health, True)
        module_ui.display_resource_bar(
            "Resource:", self.resource, self.max_resource)
        module_ui.separator()
        print(f"Attack: {module_ui.color(self.attack,'green')}")
        print(f"Defense: {module_ui.color(self.defense,'green')}")
        print(f"Magic: {module_ui.color(self.magic,'green')}")
        module_ui.separator()
        print(
            f"Exp: {module_ui.color(self.experience,'green')} / {module_ui.color(self.max_experience,'green')}")

    def equip_item(self,item):
        pass

    def unequip_item(self,item):
        # for item in equipment
        # print equipment
        # fill list_choices with item equipment
        # for unequip an item
        pass
    
    # region getter & setter
    def set_name(self, value):
        """set name"""
        self.name = value

    def set_job(self, value):
        """set job"""
        self.job = value
    # endregion
