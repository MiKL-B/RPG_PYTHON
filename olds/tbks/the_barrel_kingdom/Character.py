import module_ui


class Character:
    def __init__(
      self, name, level, health, max_health, mana,
      max_mana, strength, defense, speed, positionX, positionY):
        self._name = name
        self._level = level
        self._health = health
        self._max_health = max_health
        self._mana = mana
        self._max_mana = max_mana
        self._strength = strength
        self._defense = defense
        self._speed = speed
        self._positionX = positionX
        self._positionY = positionY


    def display_resource_bar(self,resource_text,value,max_value, is_health = False):
        dashes = 10
        dash_convert = int(max_value / dashes)
        current_dashes = int(value / dash_convert)
        remaining_resource = dashes - current_dashes
        remaining_display = ' ' * remaining_resource

        percent = (value * 100) / max_value

        if is_health:
            if percent >= 75:
                color = module_ui.GREEN
            elif percent >= 50:
                color = module_ui.YELLOW
            else:
                color = module_ui.RED
        else:
            color = module_ui.BLUE

        # square bar
        square_bar = color +"\u2588" + module_ui.END

        resource_bar = square_bar * current_dashes

        print(resource_text + " |" + resource_bar + remaining_display + "| " + color + str(value) + module_ui.END,"/",str(max_value))


    def print_info(self):
        print(f"Name: {self._name}  |  Level: {module_ui.return_text(self._level, module_ui.CYAN)}")
        self.display_resource_bar("Health:",self._health,self._max_health,True)
        self.display_resource_bar("Mana:",self._mana,self._max_mana)

    def display_info_combat(self):
        print(self._name)
        print(f"Health: {self._health} / {self._max_health}")
        print(f"Strength: {self._strength}")
        print(f"Defense: {self._defense}")
        print(f"Speed: {self._speed}")

    def increase_health(self, amount):
        self._health += amount

    def decrease_health(self, amount):
        self._health -= amount

    def increase_max_health(self, amount):
        self._max_health += amount

    def is_dead(self):
        return self._health <= 0

    def attack_target(self, target):
        target._health -= self._strength

    def is_the_fastest(self, target):
        return self._speed > target._speed

    def increase_mana(self, amount):
        self._mana += amount

    def decrease_mana(self, amount):
        self._mana -= amount

    def increase_max_mana(self, amount):
        self._max_mana += amount
