from characters.character import Character
import textwrap

class PlayerCharacter(Character):
    def __init__(self,name,hp,mp,atk,matk,defense,weapon,armor):
        super().__init__(name,hp,mp,atk,defense)
        self.matk = matk
        self.weapon = weapon
        self.armor = armor

    def attack(self,enemies):
        print("\nWho do you want to target?")
        enemy_count = 0
        for enemy in enemies:
            print(str(enemy_count) + " - " + enemy.name + "  " + str(enemy.hp) + "/" + str(enemy.full_hp)) #Prints enemy party
            enemy_count += 1
        selection = int(input())
        target = enemies[selection]
        target.hp -= (self.atk - target.defense)
        print(target.name + " took " + str(self.atk-target.defense) + " damage\n")

    #Function to equip weapon or armor. These really don't do much while playing the game, just something I was playing around with.
    def equip_weapon(self,weapon, inventory):
        self.atk += weapon.atk
        self.matk += weapon.matk
        self.weapon = weapon
        if self.weapon == None:
            pass #Ignores putting weapon into inventory
        else:
            if self.weapon.name in inventory:
                inventory[self.weapon.name] += 1 #Checks if inventory already has weapon currently equipped, if it does, it'll increment the count
            else:
                inventory[self.weapon.name] = 1 #Puts the currently equipped weapon into inventory
        if weapon.name in inventory and inventory[weapon.name] == 1:
            del inventory[weapon.name] #Removes the weapon from inventory if it was the only one
        elif weapon.name in inventory:
            inventory[weapon.name] -= 1
        print(weapon.name + " has been equipped.")

    #Pretty much same as above.
    def equip_armor(self,armor,inventory):
        self.hp += armor.hp
        self.full_hp += armor.hp
        self.defense += armor.defense
        self.armor = armor
        if self.armor == None:
            pass
        else:
            if self.armor.name in inventory:
                inventory[self.armor.name] += 1
            else:
                inventory[self.armor.name]= 1
                self.armor = armor
        if armor.name in inventory and inventory[armor.name] == 1:
            del inventory[armor.name]
        elif armor.name in inventory:
            inventory[armor.name] -= 1
        print(armor.name + " has been equipped.")

    def use_potion(self,inventory):
        print("Which potion do you want to use?")
        choice = input(textwrap.dedent("""
                        0 - Health Potion : %d
                        1 - Mana Potion : %d
                        """ % (inventory['Health Potion'],inventory['Mana Potion'])))
        if choice == "0":
            self.health_potion(inventory)
        elif choice == "1":
            self.mana_potion(inventory)

    def health_potion(self,inventory):
        if inventory['Health Potion'] == 0:
            print("You are out of health potions!")
        else:
            self.hp += 50
            if self.hp > self.full_hp: #Checks so you don't over heal.
                self.hp = self.full_hp
            inventory['Health Potion'] -= 1
            print("You used a health potion! 50 health is restored\n")

    def mana_potion(self,inventory):
        if inventory['Mana Potion'] == 0:
            print("You are out of Mana potions!")
        else:
            self.mp += 50
            if (self.mp) > self.full_mp:
                self.mp = self.full_mp
            inventory['Mana Potion'] -= 1
            print("You used a mana potion! 50 mana is restored\n")
