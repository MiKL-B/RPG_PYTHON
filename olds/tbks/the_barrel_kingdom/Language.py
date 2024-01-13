# def change_locale_language():
#   choice = Sys_UI.input_command()
#   if choice == "en":
#       locale.setlocale(locale.LC_ALL, ('en', 'UTF-8'))
#   elif choice == "fr":
#       locale.setlocale(locale.LC_ALL, ('fr', 'UTF-8'))
#   save_locale_language()

# #--------------------------------------------------------------------

# def load_locale_language():
#     Sys_UI.clear_message()
#     if get_locale_language():
#         retrieve_locale = pickle.load(open("save/SaveLocale", "rb"))
#         loc = locale.getlocale()
#         locale.setlocale(locale.LC_ALL, retrieve_locale)

# #--------------------------------------------------------------------

# def save_locale_language():
#     Sys_UI.clear_message()
#     loc = locale.getlocale()
#     data = loc
#     pickle.dump(data, open("save/SaveLocale", "wb"))
#     print("locale saved")
#     time.sleep(3)

# #--------------------------------------------------------------------

# def get_locale_language():
#     path = "save/SaveLocale"
#     isSaveFileExist = os.path.exists(path)
#     return isSaveFileExist

# #--------------------------------------------------------------------

# class Language:
#     def __init__(self,code,text):
#         self._code = code
#         self._text = text


# FRENCH = Language("fr",33)
# ENGLISH = Language("en",34)

# languages = [FRENCH,ENGLISH]

# #--------------------------------------------------------------------

# def display_languages():
#     console = Console()
#     loc = locale.getlocale()
#     sText = ""

#     list_languages = Table(title="info")
#     list_languages.add_column("col 1")
#     list_languages.add_column("col 2")
#     for index, item in enumerate(languages):
#         if loc == ('fr_FR','UTF-8'):
#             sText = I18n_Texts.i18n_french_msg[item._text]
#         else:
#             sText = I18n_Texts.i18n_english_msg[item._text]
#         list_languages.add_row(item._code,sText)

#     console = Console()
#     console.print(list_languages)

#--------------------------------------------------------------------
