import os
import pickle
import module_ui


def load():
    if player_has_data():
        data = pickle.load(open("save/SaveFile", "rb"))
        return data


def save(hero):
    module_ui.clear_console()
    pickle.dump(hero, open("save/SaveFile", "wb"))


def delete():
    module_ui.clear_console()
    os.remove("save/SaveFile")
    print(f"Deleted")


def player_has_data():
    s_path = "save/SaveFile"
    b_is_file_data_exist = os.path.exists(s_path)
    return b_is_file_data_exist
