import textwrap
from characters.classes.TempClass import TempClass
from status import battle_status, player_status
from Items.Sword import *
from Items.Armor import *
from tutorial import tutorial
from menu import menu
save_prompt = input("Input 0 to start a new game or 1 to load previous save file.\n")

if save_prompt == "0":
    inventory = {'Health Potion': 5, 'Mana Potion': 5}
    name = input("Welcome to the world's worst RPG ever tutorial! Note, this game is very unbalanced. I am no way responsible for your frustration at how hard or easy it is. What is your name?\n")
    player = TempClass(name)
    player = tutorial(player,inventory)
    #Delays so a wall of text doesn't suddenly get printed
    delay = input("Press enter to continue...\n")
    print(textwrap.dedent("""
    You are on a quest to the Dragon King's castle to save the princess of your home, America from the clutches of the evil Dragon King who wants to take her as a bride.
    He is not an easy foe to fight. By slaying his lieutenants the Skeleton King and Goblin King, you will obtain an ancient sword and ancient armor that they jealously guard.
    This will increase your powers by many folds. However, you are not quite ready yet and it is highly advised you go training, slaying minions of the Dragon King's lieutenants.
    Head forth adventurer and save your princess!"""
    ))
    menu(player,inventory)
elif save_prompt == "1":
    inventory = {'Health Potion': 0, 'Mana Potion' : 0}
    file_handle = open("save.txt", "r")

    name = file_handle.readline()
    hp = int(file_handle.readline())
    mp = int(file_handle.readline())
    atk = int(file_handle.readline())
    matk = int(file_handle.readline())
    defense = int(file_handle.readline())

    player = TempClass(name,hp,mp,atk,matk,defense)
    inventory['Health Potion'] = int(file_handle.readline())
    inventory['Mana Potion'] = int(file_handle.readline())

    #Couldn't quite figure a good way to save the weapon information...so manually equipping it is.
    bronze_sword = BronzeSword()
    bronze_plate = BronzePlate()
    player.equip_weapon(bronze_sword,inventory)
    player.equip_armor(bronze_plate,inventory)

    menu(player,inventory)
#Debugging purposes so you don't have to go through tutorial
elif save_prompt == "2":
    player = TempClass("Name",999,999,999,999)
    inventory = {'Health Potion': 5, 'Mana Potion': 5}
    bronze_sword = BronzeSword()
    bronze_plate = BronzePlate()
    player.equip_weapon(bronze_sword,inventory)
    player.equip_armor(bronze_plate,inventory)
    menu(player,inventory)

