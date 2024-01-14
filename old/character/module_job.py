"""
    represents the differents class of the hero
"""
import module_text

class Job:
    """
    represents the differents class of the hero
    """
    def __init__(self, index, name):
        self.index = index
        self.name = name

    def get_name(self)-> str:
        """get name"""
        return self.name

WARRIOR = Job(0, module_text.WARRIOR)
ROGUE = Job(1, module_text.ROGUE)
WIZARD = Job(2, module_text.WIZARD)
