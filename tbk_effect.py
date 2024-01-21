def heal(self,value):
    if self.health + value > self.max_health:
        self.health = self.max_health
    else:
        self.health += value

def cure(self,value):
    if self.state != value:
        self.state = value

def take_damage(self,value):
    self.health -= value
    if self.health <= 0:
        self.health = 0
        
def fireball():
    pass