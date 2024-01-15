import tbk_job

class Shop:
    def __init__(self,items = None,loc_x=0,loc_y=0):
        if items is None:
            items = []
        self.items = items
        self.loc_x = loc_x
        self.loc_y = loc_y

class Item:
    def __init__(self,name,purchase_price,sale_price):
        self.name = name
        self.purchase_price = purchase_price
        self.sale_price = sale_price

class Consumable(Item):
    def __init__(self,name,purchase_price,sale_price,category,value,quantity):
        Item.__init__(self,name,purchase_price,sale_price)
        self.category = category
        self.value = value
        self.quantity = quantity

class Equipment(Item):
    def __init__(self,name,purchase_price,sale_price,job_category_id):
        Item.__init__(self,name,purchase_price,sale_price)
        self.job_category_id = job_category_id

class Weapon(Equipment):
    def __init__(self,name,purchase_price,sale_price,job_category_id,attack):
        Equipment.__init__(self,name,purchase_price,sale_price,job_category_id)
        self.attack = attack

class Armor(Equipment):
    def __init__(self,name,purchase_price,sale_price,job_category_id,defense):
        Equipment.__init__(self,name,purchase_price,sale_price,job_category_id)
        self.defense = defense



# sword = Weapon("Sword",50,25,tbk_job.TYPE_FIGHT,10)
# bow = Weapon("Bow",50,25,tbk_job.TYPE_RANGE,10)
# shield = Armor("Shield",50,25,tbk_job.TYPE_FIGHT,5)
# shield = Armor("Shield",50,25,tbk_job.TYPE_FIGHT,5)
# shop = Shop([potion,sword,bow],1,0)




class P:
    def __init__(self,health,max_health,state,inventory=None):
        self.health = health
        self.max_health = max_health
        self.state = state
        if inventory == None:
            inventory = []
        self.inventory = inventory

        
    def use_item(self,item):
        if item not in self.inventory:
            print(f"You don't have {item.name} in your inventory")
            return
        
        if not isinstance(item,Consumable): 
            print(f"{item.name} is not a consumable!")
            return
        
        match item.category:
            case "heal":
                heal(self,item.value)
                print(f"Heal done: {item.value}")
            case "cure":
                cure(self,item.value)
                print(f"Cure done!")

        self.remove_item(item)
    

    def remove_item(self,item):
        if len(self.inventory) == 0:
            print("Nothing to remove, your inventory is empty!")
            return

        if item not in self.inventory:
            print(f"You don't have {item.name} in your inventory")
            return
        
        item.quantity -= 1
        print(f"{item.name} removed from inventory!")
        
        if item.quantity == 0:
            self.inventory.remove(item)


    def pickup_item(self,item):
        if len(self.inventory) == 10:
            print("Your inventory is full!")
            return
        
        if item not in self.inventory:
            self.inventory.append(item)
            return
        
        item.quantity += 1
        
        

    def refresh(self):
        for item in self.inventory:
            print(f"{item.name} qty: {item.quantity}")
        


def heal(self,value):
    if self.health + value > self.max_health:
        self.health = self.max_health
    else:
        self.health += value

def cure(self,value):
    if self.state != value:
        self.state = value



potion = Consumable("Potion",50,25,"heal",25,1)
beer = Consumable("Beer",50,25,"heal",100,1)
# antidote = Consumable("Antidote",50,25,"cure",0)

player = P(50,100,1)

player.pickup_item(potion)
player.pickup_item(potion)
player.pickup_item(beer)

player.refresh()

