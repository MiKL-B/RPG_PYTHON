def heal(self,value):
    if self.health + value > self.max_health:
        self.health = self.max_health
    else:
        self.health += value

def cure(self,value):
    if self.state != value:
        self.state = value

def fireball():
    pass