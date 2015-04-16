def fire(self,target):
    if self.mp < 10:
        print("Not enough mana")
    else:
        self.mp -= 10
        if target.name == "Goblin" or target.name == "Goblin King":     #All magic spells do triple damage against specific monster types.
            target.hp -= self.matk*6
            print(target.name + " took " + str(self.matk*6) + " damage.\n")
        else:
            target.hp -= self.matk*2
            print(target.name + " took " + str(self.matk*2) + " damage.\n")

def thunder(self,target):
    if self.mp < 10:
        print("Not enough mana")
    else:
        self.mp -= 10
        if target.name == "Bat":
            target.hp -= self.matk*6
            print(target.name + " took " + str(self.matk*6) + " damage.\n")
        else:
            target.hp -= self.matk*2
            print(target.name + " took " + str(self.matk*2) + " damage.\n")

def cure(self,target):
    self.mp -= 10
    if target.name == "Skeleton" or target.name == "Skeleton King":
        target.hp -= self.matk*6
        print(target.name + " took " + str(self.matk*6) + " damage.\n")
    else:
        target.hp += self.matk*2
        if target.hp > target.full_hp:     #Check for not overhealing
            target.hp = target.full_hp
        print(target.name + " healed " + str(self.matk*2) + "hp.\n")

def triple(self,target):
    if self.mp < 8:
        print("Not enough mana")
    else:
        self.mp -= 8
        target.hp -= (self.atk*3 - target.defense)
        print(target.name + " took " + str(self.atk*3 - target.defense) + " damage.\n")

def phalanx(self):
    if self.mp < 10:
        print("Not enough mana")
    else:
        self.defense *= 3
        print("Your defense became " + str(self.defense + "\n"))

def mana(self,target):
    if self.mp == 0:
        print("Not enough mana")
    else:
        target.hp -= (self.atk*5 + self.mp*5)
        print(target.name + " took " + str(self.atk*5 + self.mp*5) + " damage.")
        print("Your mana has been depleted.\n")
        self.mp = 0
