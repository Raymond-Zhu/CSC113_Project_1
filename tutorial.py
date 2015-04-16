from characters.enemies import Bat, Goblin, Skeleton
from Items.Sword import BronzeSword
from Items.Armor import BronzePlate
from status import player_status, battle_status
import textwrap

def tutorial(player,inventory):
    print("Let's go through a tutorial on some of the basics of the game")
    bat = Bat()
    goblin = Goblin()
    skeleton = Skeleton()
    enemies = [bat, goblin, skeleton]
    print("You have just encountered some enemies! Lets get you in some gear and see how battle works.")
    bronze_sword = BronzeSword()
    bronze_plate = BronzePlate()
    player.equip_weapon(bronze_sword,inventory)
    player.equip_armor(bronze_plate,inventory)
    print("\nYou encountered a group of enemies!")
    for enemy in enemies:
        print("A " + enemy.name + " has appeared.")
    print(textwrap.dedent("""
           Bats are flying type and take extra damage when you attack it with a lightning ability.
           Goblins are weak to fire.
           Skeletons are weak to healing magic.

           You can cast 3 magic spells: Fire, Thunder, and Cure. These should be self explanatory. They all cost 10 mana to use.

           You can cast 3 skills: Triple Slash, Phalanx, and Manaslash.
           Triple Slash: Uses 8 mana to attack three times your attack.
           Phalanx: Uses 10 mana to triple your defense
           Manaslash: Uses all your remaining mana to do tons of damage.
           """ ))
    #Below is just the battle function with extra text added.
    enemy_count = len(enemies)
    status = True
    while(status):
        choice = input(textwrap.dedent("""
                        What do you want to do?

                        0 - Attack
                        1 - Magic
                        2 - Skills
                        3 - Items
                        """))
        if choice == "0":
            player.attack(enemies)
        elif choice == "1":
            player.magic(enemies)
        elif choice == "2":
            player.skill(enemies)
        elif choice == "3":
            player.use_potion(inventory)
        status = battle_status(player,enemies)

        delay = input("Press enter to continue...\n")
        if len(enemies) is not 0:
            for enemy in enemies:
                enemy.attack(player)
            status = battle_status(player,enemies)
            delay = input("Press enter to continue...\n")
    print("You have gained %d experience." % (enemy_count))
    print("After a battle, you gain one experience point for every monster you fought. Every experience point increases your hp,mp,atk,matk,and defense by one. You also get a chance to get a potion drop.")
    for x in range(0, enemy_count):
        player.hp += 1
        player.full_hp += 1
        player.mp += 1
        player.full_mp += 1
        player.atk += 1
        player.matk += 1
        player.defense += 1
    player_status(player)

    print("\nYou have reached the end of the tutorial! Now your real adventure begins.")
    return player
