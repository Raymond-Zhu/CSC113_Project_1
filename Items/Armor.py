class Armor:
    def __init__(self,name,hp,defense):
        self.name = name
        self.hp = hp
        self.defense = defense

class BronzePlate(Armor):
    def __init__(self,name = "Bronze Plate", hp = 25, defense = 7):
        super().__init__(name,hp,defense)

class ArtifactArmor(Armor):
    def __init__(self,name = "Artifact Armor", hp = 1000, defense = 300):
        super().__init__(name,hp,defense)
