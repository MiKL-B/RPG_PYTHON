import inquirer
from tbk_singleton import Singleton
import tbk_ui
import tbk_text 
import tbk_item
import tbk_effect

class Player(metaclass=Singleton):
    def __init__(self,name="",job = None,loc_x=0, loc_y=0,health=0,max_health=0,state=0,equipment=None,inventory=None,gold=0):
        self.name = name
        self.job = job
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.health = health
        self.max_health = max_health
        self.state = state
        if equipment == None:
            equipment =  []
        self.equipment = equipment
        if inventory == None:
            inventory = []
        self.inventory = inventory
        self.gold = gold


    # region refresh
    def print_info(self):
        tbk_ui.print_msg("Name",self.name,"green")
        tbk_ui.print_msg("Job",self.job.name,"green")

    def print_gold(self):
        tbk_ui.print_msg("Gold",self.gold, "yellow")
    
    def print_inventory(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                tbk_ui.print_msg("Item",item.name,"green")
        else:
            print("Inventory empty!")

    def print_equipment(self):
        if len(self.equipment) > 0:
            for item in self.equipment:
                tbk_ui.print_msg("Item",item.name,"green")
        else:
            print("Equipment empty!")

    def print_position(self):
        tbk_ui.print_msg("X",self.loc_x,"green")
        tbk_ui.print_msg("Y",self.loc_y,"green")
    # endregion

    # region setters
    def set_name(self, question_name, answer_name):
        max_length_name = 10
        while True:
            length_name = len(answer_name["name"])
            if length_name <= max_length_name:
                break
            tbk_ui.print_msg("Name too long!","","red")
            answer_name = inquirer.prompt(question_name)

        if answer_name["name"] == "":
            answer_name["name"] = "Hero"

        self.name = answer_name["name"]
    
    def set_job(self,value):
        self.job = value
    # endregion
        
    # region move
    def move(self,x,y):
        self.loc_x += x
        self.loc_y += y

    def move_north(self):
        """move north"""
        if self.loc_y > 0:
            self.move(0, -1)
        else:
            tbk_ui.print_msg(tbk_text.IMPOSSIBLE_DIRECTION,"","red")
            tbk_ui.wait()

    def move_west(self):
        """move west"""
        if self.loc_x > 0:
            self.move(-1, 0)
        else:
            tbk_ui.print_msg(tbk_text.IMPOSSIBLE_DIRECTION,"","red")
            tbk_ui.wait()

    def move_east(self):
        """move east"""
        if self.loc_x < 10:
            self.move(1, 0)
        else:
            tbk_ui.print_msg(tbk_text.IMPOSSIBLE_DIRECTION,"","red")
            tbk_ui.wait()

    def move_south(self):
        """move south"""
        if self.loc_y < 10:
            self.move(0, 1)
        else:
            tbk_ui.print_msg(tbk_text.IMPOSSIBLE_DIRECTION,"","red")
            tbk_ui.wait()
    # endregion

    # region item
    def use_item(self,item):
        # can't use a consumable which is not in the inventory
        if item not in self.inventory:
            print(f"You don't have {item.name} in your inventory")
            return
        
        # can't use an item which is not a consumable
        if not isinstance(item,tbk_item.Consumable): 
            print(f"{item.name} is not a consumable!")
            return
        
        # process to use an item according to his category
        match item.category:
            case "heal":
                tbk_effect.heal(self,item.value)
                print(f"Heal done: {item.value}")
            case "cure":
                tbk_effect.cure(self,item.value)
                print(f"Cure done!")

        self.remove_item(item)
    
    def equip_item(self,item):
        # check if already have a weapon or armor or jewel 
        for it in self.equipment:
            if type(it) == type(item):
                print(f"you already have equipped a {type(it)}")
                return
        
        # can't equip more than three items
        if len(self.equipment) == 3:
            print("equipment full!")
            return

        # can't equip an item which is not in the inventory
        if item not in self.inventory:
            print(f"You don't have {item.name} in your inventory")
            return
        
        # check if the item is an equipment
        if not isinstance(item,(tbk_item.Weapon,tbk_item.Armor,tbk_item.Jewel)):
            print(f"{item.name} is not an equipment!")
            return
        
        # process to equip
        self.equipment.append(item)
        self.remove_item(item)
        item.quantity = 1
        print(f"{item.name} well equipped!")
    
    def unequip_item(self,item):
        # can't unequip if the equipment is empty
        if len(self.equipment) == 0:
            print("Nothing to unequip")
            return
        
        # can't unequip an item which is not equipped
        if item not in self.equipment:
            print(f"You don't have {item.name} in your equipment")
            return
        
        # process to unequip
        self.equipment.remove(item)
        self.inventory.append(item)
        item.quantity = 1
        print(f"{item.name} well unequipped!")
        
    def remove_item(self,item):
        # can't remove it the inventory is empty
        if len(self.inventory) == 0:
            print("Nothing to remove, your inventory is empty!")
            return
        
        # can't remove an item which is not in the inventory
        if item not in self.inventory:
            print(f"You don't have {item.name} in your inventory")
            return
        
        # process to remove
        item.quantity -= 1
        print(f"{item.name} removed from inventory!")
        
        if item.quantity == 0:
            self.inventory.remove(item)

    def pickup_item(self,item):
        # can't pickup an item if the inventory is full
        if len(self.inventory) == 10:
            print("Your inventory is full!")
            return
        
        if item.quantity == 99:
            print(f"You have the maximum quantity for {item.name}!")
            return
        
        # check single item for equipment
        if item in self.inventory and isinstance(item,(tbk_item.Weapon,tbk_item.Armor,tbk_item.Jewel)):
            print(f"You already have {item.name} in your inventory!")
            return
        
        # process to pick up the item
        if item not in self.inventory:
            self.inventory.append(item)
            print(f"{item.name} added to your inventory!")
            return
         
        # update the quantity if the item is in the inventory
        item.quantity += 1
    
    def buy_item(self,item):
        # can't pickup an item if the inventory is full
        if len(self.inventory) == 10:
            print("Your inventory is full!")
            return
        
        if self.gold < item.purchase_price:
            print("You don't have enough money bro!")
            return
        
        # check single item for equipment
        if item in self.inventory and isinstance(item,(tbk_item.Weapon,tbk_item.Armor,tbk_item.Jewel)):
            print(f"You already have {item.name} in your inventory!")
            return
        
        # process to pick up the item
        if item not in self.inventory:
            self.inventory.append(item)
            self.gold -= item.purchase_price
            print(f"{item.name} added to your inventory!")
            print(f"You have bought {item.name} for {item.purchase_price} gold!")
            return
         
        # update the quantity if the item is in the inventory
        self.gold -= item.purchase_price
        item.quantity += 1
        print(f"{item.name} added to your inventory!")
        print(f"You have bought {item.name} for {item.purchase_price} gold!")

    def sell_item(self,item):
        # can't remove it the inventory is empty
        if len(self.inventory) == 0:
            print("Nothing to remove, your inventory is empty!")
            return
        
        # can't remove an item which is not in the inventory
        if item not in self.inventory:
            print(f"You don't have {item.name} in your inventory")
            return
        
         # process to remove
        item.quantity -= 1
        print(f"{item.name} removed from inventory!")
        
        if item.quantity == 0:
            self.inventory.remove(item)

        self.gold += item.sale_price
        print(f"You have sold {item.name} for {item.sale_price} gold!")
    # endregion