from characters.PlayerCharacter import PlayerCharacter
from characters.classes.abilities import *
import textwrap
class TempClass(PlayerCharacter):
    def __init__(self,name,hp=100,mp=100,atk=1,matk=1,defense=1,weapon=None,armor=None):
        super().__init__(name,hp,mp,atk,matk,defense,weapon,armor)

    def magic(self,enemies):
        s =input(textwrap.dedent("""
             Which spell do you want to cast?
             0 - Fire
             1 - Thunder
             2 - Cure
             """))

        print("\nWho do you want to target?")
        enemy_count = 0
        for enemy in enemies:
            print(str(enemy_count) + " - " + enemy.name + "  " + str(enemy.hp) + "/" + str(enemy.full_hp))
            enemy_count += 1
        if s == "2":
            print(str(enemy_count) + " - " + self.name)    #Prints your own name as well so you can select yourself if you cast heal. The input for casting it on yourself will always be enemy_count
        selection = int(input())

        if s == "0":
            fire(self,enemies[selection])
        elif s == "1":
            thunder(self,enemies[selection])
        elif s == "2":
            if selection is enemy_count:     #Will target self instead of enemy
                cure(self,self)
            else:
                cure(self,enemies[selection])

    def skill(self,enemies):
        s =input(textwrap.dedent("""
                Which skill do you want to use?
                0 - Triple Slash
                1 - Phalanx
                2 - Manaslash
                """))
        if s is not "1":
            print("\nWho do you want to target?")
            enemy_count = 0
            for enemy in enemies:
                print(str(enemy_count) + " - " + enemy.name + "  " + str(enemy.hp) + "/" + str(enemy.full_hp))
                enemy_count += 1
            selection = int(input())

        if s == "0":
            triple(self,enemies[selection])
        elif s == "1":
            phalanx(self)
        elif s == "2":
            mana(self,enemies[selection])


