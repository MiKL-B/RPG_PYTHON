import os
import pickle

DIR = "save"
PATH = "save/SaveFile"


def save_data(player) -> None:
    """save the player in the save/SaveFile"""
    if not os.path.isdir(DIR):
        os.mkdir(DIR)
    with open(PATH, "wb") as file_data:
        pickle.dump(player, file_data)


def load_data():
    """load the hero from the file"""
    return pickle.load(open(PATH, "rb"))


def delete_data() -> None:
    """delete the file"""
    os.remove(PATH)


def has_save() -> bool:
    """check if a save file exists"""
    return os.path.exists(PATH)
