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

def print_message(index):
    locale_language = locale.getlocale()

    if locale_language == ('fr_FR','UTF-8'):
        s_text = module_text.fr[index]
    else:
        s_text = module_text.en[index]
    print(s_text)

def get_date():
    dt_now = datetime.now()
    my_date = dt_now.strftime("%d/%m/%Y, %H:%M:%S")
    return my_date