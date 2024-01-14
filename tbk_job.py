import tbk_text as tbk_text

TYPE_FIGHT = 0
TYPE_CASTER = 1
TYPE_RANGE = 2

class Job:
    def __init__(self,name,job_category_id):
        self.name = name
        self.job_category_id = job_category_id


warrior = Job(tbk_text.WARRIOR,TYPE_FIGHT)
wizard = Job(tbk_text.WIZARD,TYPE_CASTER)
rogue = Job(tbk_text.ROGUE,TYPE_RANGE)