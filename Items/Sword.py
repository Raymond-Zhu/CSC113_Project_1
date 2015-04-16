from Items.Weapon import Weapon

class BronzeSword(Weapon):
    count = 0
    def __init__(self):
        self.name = "Bronze Sword"
        self.atk = 10
        self.matk = 6
        self.wep_type = "Sword"

class Excalibur(Weapon):
    def __init__(self):
        self.name = "Excalibur"
        self.atk = 1000
        self.matk = 300
        self.wep_type = "Sword"

