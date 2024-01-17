import tbk_job

class Shop:
    def __init__(self,items = None,loc_x=0,loc_y=0):
        if items is None:
            items = []
        self.items = items
        self.loc_x = loc_x
        self.loc_y = loc_y

class Item:
    def __init__(self,name,purchase_price,sale_price,quantity):
        self.name = name
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.quantity = quantity

class Consumable(Item):
    def __init__(self,name,purchase_price,sale_price,quantity,category,value):
        Item.__init__(self,name,purchase_price,sale_price,quantity)
        self.category = category
        self.value = value

class Equipment(Item):
    def __init__(self,name,purchase_price,sale_price,quantity,job_category_id):
        Item.__init__(self,name,purchase_price,sale_price,quantity)
        self.job_category_id = job_category_id

class Weapon(Equipment):
    def __init__(self,name,purchase_price,sale_price,quantity,job_category_id,attack):
        Equipment.__init__(self,name,purchase_price,sale_price,quantity,job_category_id)
        self.attack = attack

class Armor(Equipment):
    def __init__(self,name,purchase_price,sale_price,quantity,job_category_id,defense):
        Equipment.__init__(self,name,purchase_price,sale_price,quantity,job_category_id)
        self.defense = defense

class Jewel(Equipment):
    def __init__(self,name,purchase_price,sale_price,quantity,job_category_id,defense):
        Equipment.__init__(self,name,purchase_price,sale_price,quantity,job_category_id)
        self.defense = defense
    





# shop = Shop([potion,sword,bow],1,0)




class P:
    def __init__(self,health,max_health,state,equipment=None,inventory=None):
        self.health = health
        self.max_health = max_health
        self.state = state
        if equipment == None:
            equipment =  []
        self.equipment = equipment
        if inventory == None:
            inventory = []
        self.inventory = inventory

        
    def use_item(self,item):
        # can't use a consumable which is not in the inventory
        if item not in self.inventory:
            print(f"You don't have {item.name} in your inventory")
            return
        
        # can't use an item which is not a consumable
        if not isinstance(item,Consumable): 
            print(f"{item.name} is not a consumable!")
            return
        
        # process to use an item according to his category
        match item.category:
            case "heal":
                heal(self,item.value)
                print(f"Heal done: {item.value}")
            case "cure":
                cure(self,item.value)
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
        if not isinstance(item,(Weapon,Armor,Jewel)):
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
        
        # check single item for equipment
        if item in self.inventory and isinstance(item,(Weapon,Armor,Jewel)):
            print(f"You already have {item.name} in your inventory!")
            return
        
        # process to pick up the item
        if item not in self.inventory:
            self.inventory.append(item)
            print(f"{item.name} added to your inventory!")
            return
         
        # update the quantity if the item is in the inventory
        item.quantity += 1
        

    def refresh_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            # print(item.__dict__)
            print(f"{item.name}: {type(item)}")
        print()
    

    def refresh_weapon(self):
        print("Weapon:")
        if self.weapon != "":
            print(self.weapon.name)
        print()


    def refresh_equipment(self):
        print("Equipment:")
        for item in self.equipment:
            # print(item.__dict__)
            print(f"{item.name}: {type(item)}")
        print()


def heal(self,value):
    if self.health + value > self.max_health:
        self.health = self.max_health
    else:
        self.health += value

def cure(self,value):
    if self.state != value:
        self.state = value


sword = Weapon("Sword",50,25,1,tbk_job.TYPE_FIGHT,10)
bow = Weapon("Bow",50,25,1,tbk_job.TYPE_RANGE,10)
shield = Armor("Shield",50,25,1,tbk_job.TYPE_FIGHT,5)
potion = Consumable("Potion",50,25,1,"heal",25)
beer = Consumable("Beer",50,25,1,"heal",100)
antidote = Consumable("Antidote",50,25,1,"cure",0)
ring = Jewel("Ring",50,25,1,tbk_job.TYPE_FIGHT,5)

player = P(50,100,1)



player.pickup_item(potion)
player.pickup_item(sword)
player.pickup_item(sword)