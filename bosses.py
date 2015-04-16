from characters.classes.TempClass import TempClass
from characters.enemies import Bat, Goblin, Skeleton, DragonKing
from battle import battle
from Items.Armor import ArtifactArmor
from Items.Sword import Excalibur

def boss_battle(player,inventory):
    print("Ignoring the voice, you enter the first floor of the castle and encounter the fat Goblin King. He yells  YOU SHALL NOT PASS and engages you in batle.\n")
    enemies = []
    #Goblin King Fight
    for x in range(0,4):
        goblin = Goblin()
        enemies.append(goblin)
    goblin_king = Goblin("Goblin King",500, 500, 30, 10)
    enemies.append(goblin_king)
    battle(player,enemies,inventory)
    if player.hp <= 0:
        return
    print("After slaying the Goblin King, you find in his treasure room an old stone sword. This is the sword of legend, Excalibur. However its true power will be revealed after you obtain the ancient armor.\n")
    delay = input("Press enter to continue...\n")
    print("You proceed to the second floor. The moment you step through the door to the Skeleton King's room, him and his minions launch themselves at you.\n")
    #Skeleton King Fight
    for x in range(0,4):
        skeleton = Skeleton()
        enemies.append(skeleton)
    skeleton_king = Goblin("Skeleton King",500, 500, 30, 10)
    enemies.append(skeleton_king)
    battle(player,enemies,inventory)
    if player.hp <= 0:
        return
    print("The Skeleton King has been slain and you take the Artifact Armor, off his dead body. The armor and Excalibur both glow in a blinding light. Their power has been restored! Put them on and proceed to the last floor.\n")
    delay = input("Press enter to continue...\n")
    excalibur = Excalibur()
    af_armor = ArtifactArmor()
    player.equip_weapon(excalibur,inventory)
    player.equip_armor(af_armor,inventory)
    #Dragon King Fight
    print("\nYou have reached the final floor! The dragon compliments you on reaching this far. He unleashes a loud roar and charges.\n")
    dragon = DragonKing()
    enemies.append(dragon)
    battle(player,enemies,inventory)
    if player.hp <= 0:
        return
    print("Congratulations! You beat the dragon king! You saved the princess and she falls in love with you and marries and yada yada yada. You live happily ever after. The end!\n")

def boss_battle2(player,inventory):
    print("\nThe mysterious voice says \"You have made the right choice.\" You feel power swelling through you. You grow wings that allow you to fly straight up to the final floor and confront the dragon king.")
    player = TempClass(player.name,1000000,100000,1000000,100000,1000000,player.weapon,player.armor)
    delay = input("\nPress enter to continue...\n")
    print("The Dragon King roars and attacks you.\n")
    dragon = DragonKing()
    enemies = [dragon]
    battle(player,enemies,inventory)
    print("\nYou have defeated the Dragon King! But suddenly the mysterious voice starts laughing. \"Thank you for destroying my greatest rival. With his death, I can finally return, and you will be my vessel.\"")
    delay = input("\nPress enter to continue...\n")
    print("You are covered in smoke and transformed into a demonoid being. You cannot control your body and you watch helplessly as the mysterious entity that stole your body kills the princess.")
    print("It summoned it's demon comrades and together they covered the Earth in darkness. The rule of the demons have come...and it was all your fault. Maybe you should choose better next time. THE END.")





