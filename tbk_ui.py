"""function to interact with the terminal"""
import os
import time

from sys import platform


YELLOW = '\033[1;33m'
GREEN = '\033[1;32m'
RED = '\033[1;31m'
BLUE = '\033[1;34m'
CYAN = '\033[1;36m'
MAGENTA = '\033[1;35m'
ITALIC = "\x1B[3m"
END = '\033[0m'


def clear():
    """clear the terminal"""
    if platform in {"linux", "darwin"}:
        os.system("clear")
    else:
        os.system('cls')


def wait():
    """wait a time to display some text"""
    time.sleep(2)



def print_msg(field,value="",color=""):
    match color:
        case "green":
            color = GREEN
        case "blue":
            color = BLUE
        case "yellow":
            color = YELLOW
        case "red":
            color = RED
        case "cyan":
            color = CYAN
        case "magenta":
            color = MAGENTA
    
    text_field = color + str(field) + END
    if value != "":
        field += ":"
        text_field = str(field)

    text_value = color + str(value) + END
    print(text_field,text_value)

def print_title(title):
    clear()
    print(title)
    print()

def print_resource_bar(resource_text, value, max_value, is_health=False):
    """display resource bar"""
    dashes = 10
    dash_convert = int(max_value / dashes)
    current_dashes = int(value / dash_convert)
    remaining_resource = dashes - current_dashes
    remaining_display = ' ' * remaining_resource

    percent = (value * 100) / max_value

    if is_health:
        if percent >= 75:
            my_color = GREEN
        elif percent >= 50:
            my_color = YELLOW
        else:
            my_color = RED
    else:
        my_color = BLUE

    # square bar
    square_bar = my_color + "\u2588" + END

    resource_bar = square_bar * current_dashes

    print(resource_text + " |" + resource_bar + remaining_display +
          "| " + my_color + str(value) + END, "/", str(max_value))
