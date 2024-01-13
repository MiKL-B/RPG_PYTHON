from Item import aList_item
from rich.table import Table
from rich.console import Console


class Shop:
    def __init__(self, name):
        self._name = name
        self._stock_item = []

    def display_shop_info(self):
        table_shop = Table(title=self._name)
        table_shop.add_column("index")
        table_shop.add_column("name")
        table_shop.add_column("category")
        table_shop.add_column("price")

        if len(self._stock_item) > 0:
            for index, item in enumerate(self._stock_item):
                table_shop.add_row(str(item._index), item._name,
                                   item._category, str(item._price))
            console = Console()
            console.print(table_shop)
        else:
            print("the shop is empty")


my_shop = Shop("Boutique")
my_shop._stock_item = aList_item
