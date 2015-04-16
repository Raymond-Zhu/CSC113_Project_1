import random
from characters.enemies import Bat, Goblin, Skeleton
from battle import battle

#Generates a random enemy party for you to fight against.
def random_battle(player,inventory):
    enemy_count = random.randrange(2,5)
    enemies = []
    for x in range (0,enemy_count):
        s = random.randrange(0,3)
        if s == 0:
            goblin = Goblin()
            enemies.append(goblin)
        elif s == 1:
            bat = Bat()
            enemies.append(bat)
        elif s == 2:
            skeleton = Skeleton()
            enemies.append(skeleton)
    return battle(player,enemies,inventory)
