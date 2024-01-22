import tbk_ui
def heal(self,value):
    is_effect_done = False
    if self.health == self.max_health:
        print("You are already in good health!")
        tbk_ui.wait()
        return
    
    if self.health + value >= self.max_health:
        self.health = self.max_health
        is_effect_done = True
        print("Heal done!")
    else:
        self.health += value
        is_effect_done = True
        print("Heal done!")
    return is_effect_done

def cure(self,value):
    if self.state != value:
        self.state = value

def take_damage(self,value):
    self.health -= value
    if self.health <= 0:
        self.health = 0
        
def fireball(): # TODO
    pass
