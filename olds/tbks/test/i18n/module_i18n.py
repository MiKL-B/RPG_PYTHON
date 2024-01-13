import os
import pickle
import locale

def change_locale(code_locale):
    locale.setlocale(locale.LC_ALL, (code_locale,'UTF-8'))
    save_locale()


def load_locale():
    if player_has_locale():
        data_locale = pickle.load(open("save/SaveLocale","rb"))
        locale = locale.getlocale()
        locale.setlocale(locale.LC_ALL, data_locale)


def save_locale():
    data_locale = locale.getlocale()
    pickle.dump(data_locale, open("save/SaveLocale","wb"))


def player_has_locale():
    s_path = "save/SaveLocale"
    b_is_file_locale_exist = os.path.exists(s_path)
    return b_is_file_locale_exist
