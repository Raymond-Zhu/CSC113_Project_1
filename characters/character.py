class Character:
    def __init__(self,name,hp,mp,atk,defense):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.defense = defense
        self.full_hp = hp
        self.full_mp = mp

    def attack(self,target):
        if self.atk < target.defense:   #Guarantees that the monster does at least one damage even if it's attack is lower then player's defense
            target.hp -= 1
            print(target.name + " took 1 damage\n")
        else:
            target.hp -= (self.atk - target.defense)
            print(self.name + " did " + str(self.atk-target.defense) + " damage to " + target.name)

