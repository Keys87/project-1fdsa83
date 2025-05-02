import potions, weapons, random

class Char():
    def __init__(self, name:str, hp:int=1, dfn:int=1, atk:int=1, level:int=1, tujin:int=0, inventory:list[str]=["", "", "", "", ""]):
        self.name = name
        self.hp = hp
        self.dfn = dfn
        self.atk = atk
        self.level = level
        self.tujin = tujin
        self.inventory = inventory

class Structure():
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Player(Char):
    def __init__(self, name, hp, dfn, atk, level, tujin, inventory):
        super().__init__(name, hp, dfn, atk, level, tujin, inventory)

    def attack(self, enemy_reference, atk, equipment_reference):
        final_atk = atk + (int(equipment_reference.atk)*equipment_reference.level)
        final_atk += int(equipment_reference.attr.atk)

        print(f"{self.name} attacked {enemy_reference.name} with {equipment_reference.name}")
        enemy_reference.attacked(final_atk)

    def attacked(self, effect:dict):
        for i in effect.keys():
            setattr(self, i, int(getattr(self, i)) -  int(effect.get(i)))
    
    # example_dict = {
    #     "hp": "-10",
    # }


    def consume(self, object_reference):
        if object_reference.form == "fluid":
            verb_choice = "drink"
            object_reference.affect(self)
            print(f"{self.name} {verb_choice} {object_reference.name}")
        else:
            verb_choice = "eat"
            object_reference.affect(self)
            print(f"{self.name} {verb_choice} {object_reference.name}")

class Enemy(Char):
    def __init__(self, name, hp = 50, dfn = 10, atk = 6, level = 1, tujin = 100):
        super().__init__(name, hp, dfn, atk, level, tujin)

    def attacked(self, effect:dict):
        for i in effect.keys():
            setattr(self, i, int(getattr(self, i)) -  int(effect.get(i)))
            
    # example_dict = {
    #     "hp": "-10",
    # }

    def attack(self, enemy_reference, atk, equipment_reference):
        final_atk = atk + (int(equipment_reference.atk)*equipment_reference.level)
        final_atk += int(equipment_reference.attr.atk)

        print(f"{self.name} attacked {enemy_reference.name} with {equipment_reference.name}")
        enemy_reference.attacked(final_atk)

class Trader(Char):
    def __init__(self, name, tujin):
        # self.name = name
        # self.tujin = tujin
        super().__init__(name, tujin=tujin)

    def buy(self, customer_reference):
        def trade(product, customer_reference):
            print(f"one {product.name} for {customer_reference.name}")
            for i in range(len(customer_reference.inventory)):
                if customer_reference.inventory[i - 1] == "":
                    customer_reference.inventory[i - 1] = product
                    break

        trade_list = [ben_dao, healing_1]

        for i in trade_list:
            print(i.name)
        
        want = input("Do you want to buy something?\n")
        for i in trade_list:
            if i.name == want:
                trade(i, customer_reference=customer_reference)

ben_dao = weapons.Sword("Ben Dao", "Sword", 1, {"atk": "10"})
healing_1 = potions.PotionHealing("fluid", "water")
new_player = Player(input("Name: "), random.randint(90, 120), random.randint(10, 50), random.randint(10, 50), 1, 100, ["", "", "", "", ""])
new_trader = Trader("tester", 10)
new_enemy = Enemy("Bandit Kao")

print(new_player)
while True:
    print(eval(input("debug code: ")))

