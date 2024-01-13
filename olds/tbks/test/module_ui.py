import os
import time
from sys import platform
import locale
from datetime import datetime

import i18n.module_text as module_text
import i18n.module_i18n as module_i18n

# colors
YELLOW = '\033[1;33m'
GREEN = '\033[1;32m'
RED = '\033[1;31m'
BLUE = '\033[1;34m'
CYAN = '\033[1;36m'
MAGENTA = '\033[1;35m'
ITALIC = "\x1B[3m"
END = '\033[0m'


def clear_console():
    if platform == "linux":  # Linux
        os.system("clear")
    elif platform == "darwin":  # Mac
        os.system("clear")
    elif platform == "win32":  # Windows
        os.system("cls")


def print_message(index):
    locale_language = locale.getlocale()

    if locale_language == ('fr_FR','UTF-8'):
        s_text = module_text.fr[index]
    else:
        s_text = module_text.en[index]
    print(s_text)


def input_command():
    return input("Input a command: ").lower()


def print_separator():
    print("")


def wait(second):
    time.sleep(second)


def get_date():
    dt_now = datetime.now()
    my_date = dt_now.strftime("%d/%m/%Y, %H:%M:%S")
    return my_date
