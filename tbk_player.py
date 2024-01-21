import inquirer
from tabulate import tabulate
from tbk_singleton import Singleton
import tbk_ui
import tbk_text 
import tbk_item
import tbk_effect
import tbk_level

class Player(metaclass=Singleton):
    def __init__(self,name="",job=None,loc_x=0, loc_y=0,health=100,max_health=100,
                 state=0,equipment=None,inventory=None,gold=0,level=1,experience=0,
                 world_map_x=0,world_map_y=0):
        # player
        self.name = name
        self.job = job
        self.health = health
        self.max_health = max_health
        self.state = state
        if equipment == None:
            equipment =  []
        self.equipment = equipment
        self.level = level
        self.experience = experience
        # if heroes is None:
        #     heroes = []
        # self.heroes = heroes
        self.world_map_x = world_map_x
        self.world_map_y = world_map_y
        self.loc_x = loc_x
        self.loc_y = loc_y
        if inventory == None:
            inventory = []
        self.inventory = inventory
        self.gold = gold
        
        # if quests is None:
        #     quests = []
        # self.quests = quests
        

    # def refresh(self):
    #     """refresh info player + heroes of player"""
    #     for hero in self.heroes:
    #         print(f"Name: {hero.name} Class: {hero.job}")
    #     print(f"Gold: {module_ui.color(self.get_gold(),'yellow')}")
        
    # region refresh
    def print_info(self):
        tbk_ui.print_msg("Name",self.name,"green")
        tbk_ui.print_msg("Job",self.job.name,"green")
        tbk_ui.print_msg("Level",str(self.level),"green")
        self.print_experience()
        tbk_ui.print_msg("Health",str(self.health) + " / " + str(self.max_health), "green")
    # endregion
        
    def print_equipment(self):
        if len(self.equipment) > 0:
            for item in self.equipment:
                tbk_ui.print_msg("Item",item.name,"green")
        else:
            print("Equipment empty!")
    
    def print_experience(self):
        max_experience = tbk_level.levels[self.level-1]['max_experience']
        tbk_ui.print_msg("Exp", str(self.experience) + " / " + str(max_experience),"green")
    
    def print_gold(self):
        tbk_ui.print_msg("Gold",str(self.gold), "yellow")
    
    def print_inventory(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                tbk_ui.print_msg("Item",item.name + " x"+str(item.quantity),"green")
        else:
            print("Inventory empty!")

    def print_consumable(self):
        for item in self.inventory:
            if isinstance(item,tbk_item.Consumable): 
                print(f"{item.name}")

    def print_equipable(self):
        for item in self.inventory:
            if isinstance(item, (tbk_item.Armor, tbk_item.Weapon)):
                print(f"{item.name}")
    
    def print_position(self):
        tbk_ui.print_msg("world X",str(self.world_map_x),"green")
        tbk_ui.print_msg("world Y",str(self.world_map_y),"green")
        tbk_ui.print_msg("local X",str(self.loc_x),"green")
        tbk_ui.print_msg("local Y",str(self.loc_y),"green")
    
    # def refresh_position(self):
    #     """refresh position"""
    #     location_name = module_text.UNKNOWN
    #     for item in locations:
    #         if item.x == self.location_x and item.y == self.location_y:
    #             location_name = item.name
    #     print(f"Local:{location_name}")
    #     print(f"X:{self.location_x} Y:{self.location_y}")

    # def is_in_town(self) -> bool:
    #     """return if the player is in town for access to shop..."""
    #     in_town = False
    #     for item in locations:
    #         if item.x == self.location_x and item.y == self.location_y and item.shop:
    #             in_town = True
    #     return in_town
    # endregion
    
    # region getters
    def get_list_consumable(self):
        list_items = []
        for item in self.inventory:
            if isinstance(item,tbk_item.Consumable): 
                list_items.append(item)
        return list_items

    def get_list_equipable(self):
        list_items = []
        for item in self.inventory:
            if isinstance(item,(tbk_item.Armor,tbk_item.Weapon)):
                list_items.append(item)
        return list_items
    
    def get_list_equipment(self):
        list_items = []
        for item in self.equipment:
            list_items.append(item)
        return list_items
    
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
         # change south
        if self.loc_x == 5 and self.loc_y == 10:
            self.change_zone(0, 1)
            self.loc_x = 5
            self.loc_y = 1
        # change north
        elif self.loc_x == 5 and self.loc_y == 0:
            self.change_zone(0, -1)
            self.loc_x = 5
            self.loc_y = 9
        # change east
        elif self.loc_x == 10 and self.loc_y == 5:
            self.change_zone(1, 0)
            self.loc_x = 1
            self.loc_y = 5
        # change west
        elif self.loc_x == 0 and self.loc_y == 5:
            self.change_zone(-1, 0)
            self.loc_x = 9
            self.loc_y = 5
      
    def change_zone(self, x, y):
        """change_zone"""
        self.world_map_x += x
        self.world_map_y += y

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
            tbk_ui.wait()
            return
        
        # can't use an item which is not a consumable
        if not isinstance(item,tbk_item.Consumable): 
            print(f"{item.name} is not a consumable!")
            tbk_ui.wait()
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
                tbk_ui.wait()
                return
        
        # can't equip more than three items
        if len(self.equipment) == 3:
            print("equipment full!")
            tbk_ui.wait()
            return

        # can't equip an item which is not in the inventory
        if item not in self.inventory:
            print(f"You don't have {item.name} in your inventory")
            tbk_ui.wait()
            return
        
        # check if the item is an equipment
        if not isinstance(item,(tbk_item.Weapon,tbk_item.Armor,tbk_item.Jewel)):
            print(f"{item.name} is not an equipment!")
            tbk_ui.wait()
            return
        
        # process to equip
        self.equipment.append(item)
        self.remove_item(item)
        item.quantity = 1
        print(f"{item.name} well equipped!")
        tbk_ui.wait()
    
    def unequip_item(self,item):
        # can't unequip if the equipment is empty
        if len(self.equipment) == 0:
            print("Nothing to unequip")
            tbk_ui.wait()
            return
        
        # can't unequip an item which is not equipped
        if item not in self.equipment:
            print(f"You don't have {item.name} in your equipment")
            tbk_ui.wait()
            return
        
        # process to unequip
        self.equipment.remove(item)
        self.inventory.append(item)
        item.quantity = 1
        print(f"{item.name} well unequipped!")
        tbk_ui.wait()
        
    def remove_item(self,item):
        # can't remove it the inventory is empty
        if len(self.inventory) == 0:
            print("Nothing to remove, your inventory is empty!")
            tbk_ui.wait()
            return
        
        # can't remove an item which is not in the inventory
        if item not in self.inventory:
            print(f"You don't have {item.name} in your inventory")
            tbk_ui.wait()
            return
        
        # process to remove
        item.quantity -= 1
        print(f"{item.name} removed from inventory!")
        tbk_ui.wait()
        
        if item.quantity == 0:
            self.inventory.remove(item)

    def pickup_item(self,item):
        max_length_inventory = 10
        max_qty_item = 99
        # can't pickup an item if the inventory is full
        if len(self.inventory) == max_length_inventory:
            print("Your inventory is full!")
            return
        
        if item.quantity == max_qty_item:
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
        max_length_inventory = 10
        max_qty_item = 99
        # can't pickup an item if the inventory is full
        if len(self.inventory) == max_length_inventory:
            print("Your inventory is full!")
            return
        
        if item.quantity == max_qty_item:
            print(f"You have the maximum quantity for {item.name}!")
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
    
    def compare_item(self,item1, item2):
        headers = ["Fields", item1.name, item2.name]
        table = []

        if isinstance(item1, tbk_item.Weapon) and isinstance(item2, tbk_item.Weapon):
            table.append(["Attack", item1.attack, self.compare(item1.attack,item2.attack)])
            print(tabulate(table, headers, tablefmt="pretty"))
        elif isinstance(item1, (tbk_item.Armor, tbk_item.Jewel)) and isinstance(item2, (tbk_item.Armor, tbk_item.Jewel)):
            table.append(["Defense", item1.defense,self.compare(item1.defense, item2.defense)])
            print(tabulate(table, headers, tablefmt="pretty"))
        else:
            print("No comparison!")

    def compare(self,value1, value2):
        text = value2
        if value1 < value2:
            text = tbk_ui.GREEN + str(text) + tbk_ui.END
        elif value1 > value2:
            text = tbk_ui.RED + str(text) + tbk_ui.END
        return text
    # endregion

    # region gold
    def increase_gold(self,value):
        max_gold = 999_999
        self.gold += value
        if self.gold >= max_gold:
            self.gold = max_gold
            print(f"You have reached the maximum amount of gold!")

    def decrease_gold(self,value):
        min_gold = 0
        self.gold -= value
        if self.gold <= min_gold:
            self.gold = min_gold
    # endregion
            
    # region experience
    def increase_experience(self,value):
        # for heroes
        self.experience += value
        
        last_index = len(tbk_level.levels)-1
        if self.level == tbk_level.levels[last_index]["level"]:
            print("you have reached the maximum level")
            self.experience = tbk_level.levels[last_index]["max_experience"]
            return
        
        # increase level when you reach the the max_exp for the current level 
        if self.experience >= tbk_level.levels[self.level-1]["max_experience"]:
            self.increase_level()
             
    def increase_level(self):
        # for heroes
        self.level += 1
        self.experience = 0
        self.max_health += percentage(self.max_health,25)
    # endregion


# move to a calcul file
def percentage(field,value):
    return int(field * (value / 100))


p = Player()
