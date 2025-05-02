class Equipment():
    def __init__(self, name:str, type:str, level:int, attr:dict):
        self.name = name
        self.type = type
        self.level = level
        self.attr = attr
    
    def equip(self, object_reference):
        print(f"{object_reference.name} equips {self.name}")

class Sword(Equipment):
    def __init__(self, name:str, type:str, level:int, attr:dict):
        super().__init__(name, type, level, attr)
        
    def equip(self, object_reference, level):
        super().equip(object_reference)
        object_reference.atk += 10 * level
        object_reference.inventory[0] = "Ben Xing"
    
    
    

# example of a dictionary of attributes
# attr = {
#     "atk": 10,
#     "def": 5,
# }