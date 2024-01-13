import os
import time
from sys import platform
import module_text
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
    print(module_text.english_text[index])

def input_command():
    return input("Input a command: ").lower()


def print_separator():
    print("")


def error_message(sMessage):
    print(RED + sMessage + END)


def return_text(sMessage, sColor):
    return sColor + str(sMessage) + END

# to avoid instant refresh


def wait(iSecond):
    time.sleep(iSecond)


def help_color():
    print("increase:")
    print("value ->", return_text("value", GREEN))
    print_separator()
    print("decrease:")
    print("value ->", return_text("value", RED))
    print_separator()
    print("variable:")
    print("value ->", return_text("value", CYAN))
    print_separator()
    print("gold:")
    print("value ->", return_text("value", YELLOW))
    print_separator()
    print("loot:")
    print("value ->", "[value]")
    print("value ->", return_text("[value]", GREEN))
    print("value ->", return_text("[value]", BLUE))
    print("value ->", return_text("[value]", MAGENTA))
# ==========================================================



# ==========================================================

# class Message:
#     def __init__(self,text,command=False):
#         self._text = text
#         self._command = command


#     def get_text_current_language(self):
#         console = Console()
#         loc = locale.getlocale()
#         sText = ""

#         if loc == ('fr_FR','UTF-8'):
#             sText = I18n_Texts.i18n_french_msg[self._text]
#         else:
#             sText = I18n_Texts.i18n_english_msg[self._text]
#         return sText


#     def print_title(self):
#         print('{:^70}'.format(sText.upper()))


#     def get_command(self):
#         return self.get_text_current_language()[0].lower()


#     def print_command(self):
#         return Sys_Color.BLUE + "[" + self.get_text_current_language()[0].upper() + "]" + Sys_Color.END_COLOR


#     def error_message(self):
#         print(Sys_Color.RED + self.get_text_current_language() + Sys_Color.END_COLOR)
#         time.sleep(2)


#     def print_message(self):
#         sText = self.get_text_current_language()
#         if self._command:
#             print(self.print_command(),'{:<70}'.format(sText))
#         else:
#             print('{:<70}'.format(sText))

# #--------------------------------------------------------------------
