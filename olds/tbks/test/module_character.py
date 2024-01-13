import module_ui


class Character:
    def __init__(self):
        self._name = ""
        self._level = 1
        self._health = 50
        self._max_health = 50
        self._strength = 1
        self._defense = 1
        self._speed = 1
        self._y = 0
        self._x = 0


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


    def info(self):
        print(f"Name: {self.get_name()} | Level: {self.get_level()}")
        self.display_resource_bar("Health:",self.get_health(),self.get_max_health(),True)
        # self.display_resource_bar("Mana:",self._mana,self._max_mana)
        module_ui.print_separator()
        print(f"Strength: {self.get_strength()}")
        print(f"Defense: {self.get_defense()}")
        print(f"Speed: {self.get_speed()}")


    def get_name(self):
        return self._name


    def get_level(self):
        return self._level


    def get_health(self):
        return self._health


    def get_max_health(self):
        return self._max_health


    def get_strength(self):
        return self._strength


    def get_defense(self):
        return self._defense


    def get_speed(self):
        return self._speed
