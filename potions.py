class Potion():
    def __init__(self, form, name):
        self.name = name
        self.form = "fluid"

        # here add the effect based on the type
        # example
        # affected_reference.att += 10

class PotionHealing(Potion):
    def __init__(self, form:str, name:str):
        super().__init__(form, name)
        self.name = "Potion of Healing"

    def affect(self, affected_reference):
        affected_reference.hp += 10

class PotionAttack(Potion):
    def __init__(self, form:str, name:str):
        super().__init__(form, name)
        self.name = "Potion of Attack"
    
    def affect(self, affected_reference):
        affected_reference.att += 10