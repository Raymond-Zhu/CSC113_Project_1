from status import player_status, battle_status #battle_status checks the status of everyone after someone makes a turn. If all enemy hp is 0 or player's hp is 0, it returns false to break the loop ending the battle
import random
import textwrap

def battle(player,enemies,inventory):
    for enemy in enemies:
        print("A " + enemy.name + " has appeared.")
    enemy_count = len(enemies)
    delay = input("\nPress enter to continue...")
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

        delay = input("\nPress enter to continue...\n")
        if len(enemies) is not 0:
            for enemy in enemies:
                enemy.attack(player)
            status = battle_status(player,enemies)
            delay = input("\nPress enter to continue...\n")
        #Returns when you died
        if player.hp <= 0:
            return player
    print("You have gained %d experience.\n" % (enemy_count))

    for x in range(0,enemy_count):
        player.hp += 1
        player.full_hp += 1
        player.mp += 1
        player.full_mp += 1
        player.atk += 1
        player.matk += 1
        player.defense += 1
    player_status(player)

    #Random potion drop
    drop = random.randrange(0,4)
    if drop == 0:
        inventory['Health Potion'] += 1
        print("You have obtained a Health Potion!\n")
    elif drop == 2:
        inventory['Mana Potion'] += 1
        print("You have obtained a Mana Potion!\n")
    return player
