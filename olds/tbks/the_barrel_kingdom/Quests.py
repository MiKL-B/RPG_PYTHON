from rich.table import Table
from rich.console import Console


class Quest():
    def __init__(self, index, name, description):
        self._index = index
        self._name = name
        self._description = description
        # self._status = status
        # self.reward = reward


def display_quest_info():
    table_quest = Table(title="Quests")
    table_quest.add_column("Index")
    table_quest.add_column("Name")
    table_quest.add_column("Description")

    if len(list_quest) > 0:
        for index, item in enumerate(list_quest):
            table_quest.add_row(
                str(item._index), item._name, item._description)
        console = Console()
        console.print(table_quest)
    else:
        print("the quest list is empty")


quest = Quest(2, "Le Dwagon", "Tuer le dwagon")
list_quest = [quest]
