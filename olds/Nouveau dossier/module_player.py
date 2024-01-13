import  module_item

class Player:
    def __init__(self,name = "",inventory = None, weapon = None):
        self.name = name
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
        self.weapon = weapon

    def refresh(self):
        print(self.name)

    def refresh_inventory(self):
        if len(self.inventory) == 0:
            print("Inventory empty!")
            return
        for item in self.inventory:
            print(item.name)
    
    def refresh_equipable_items(self):
        for item in self.inventory:
            if isinstance(item, (module_item.Weapon)):
                self.refresh_info_item(item)

    def get_list_equipable(self):
        list_items = []
        for item in self.inventory:
            if isinstance(item, (module_item.Weapon)):
                list_items.append(item)
        return list_items
                
    def refresh_info_item(self,item):
        print(item.name)

    def equip(self,item):
        self.inventory.remove(item)
        self.weapon = item

    def unequip(self,item):
        self.weapon = None 
        self.inventory.append(item)

    def get_weapon(self):
        if not self.weapon:
            print("No weapon!")
            return
        print(self.weapon.name)
