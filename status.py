import textwrap

def battle_status(player,enemies):
    if player.hp <= 0:
        print("\nYou have been defeated! Game over!")
        return False
    else:
        print("\nYou have %d hp out of %d hp remaining."% (player.hp,player.full_hp))
        print("You have %d mp out of %d mp remaining.\n" % (player.mp,player.full_mp))
    for enemy in enemies:
        if enemy.hp <= 0:
            print(enemy.name + " has been defeated!")
        else:
            print("%s has %d hp remaining" %(enemy.name,enemy.hp))
    #Checks if enemies have been killed. If they have, removes them from the enemy "party."
    for enemy in enemies:
        if enemy.hp <= 0:
            enemies.remove(enemy)
    if not enemies:
        print("You have defeated all your enemies!\n")
        return False
    return True

#Player stats
def player_status(player):
    print(textwrap.dedent("""
            Your current stats are:
            HP: %d/%d
            MP: %d/%d
            ATK: %d
            MATK: %d
            DEF: %d
            WEAPON: %s
            ARMOR: %s
            """ % (player.hp, player.full_hp,player.mp,player.full_mp,player.atk,player.matk,player.defense,player.weapon.name,player.armor.name)))
