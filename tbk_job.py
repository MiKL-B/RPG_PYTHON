import tbk_text

TYPE_FIGHT = 0
TYPE_CASTER = 1
TYPE_RANGE = 2

class Job:
    def __init__(self,name,job_category_id,attack,defense):
        self.name = name
        self.job_category_id = job_category_id
        self.attack = attack
        self.defense = defense


warrior = Job(tbk_text.WARRIOR,TYPE_FIGHT,1,1)
wizard = Job(tbk_text.WIZARD,TYPE_CASTER,2,2)
rogue = Job(tbk_text.ROGUE,TYPE_RANGE,3,3)