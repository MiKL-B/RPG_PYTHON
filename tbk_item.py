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
    def __init__(self,name,purchase_price,sale_price,effect):
        Item.__init__(self,name,purchase_price,sale_price)
        self.effect = effect


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



potion = Consumable("Potion",50,25,150)
sword = Weapon("Sword",50,25,tbk_job.TYPE_FIGHT,10)
bow = Weapon("Bow",50,25,tbk_job.TYPE_RANGE,10)
shield = Armor("Shield",50,25,tbk_job.TYPE_FIGHT,5)

shop = Shop([potion,sword,bow],1,0)


class P:
    def __init__(self,health,max_health):
        self.health = health
        self.max_health = max_health

    def heal(self,value):
        if self.health + value > self.max_health:
            self.health = self.max_health
        else:
            self.health += value
    
    # def damage(self,value):




player = P(50,100)

print(player.__dict__)
player.heal(potion.effect)
print("heal done")
print(player.__dict__)