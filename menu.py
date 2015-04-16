import textwrap
from status import player_status
from random_battle import random_battle
from save import save
from bosses import boss_battle, boss_battle2

def menu(player,inventory):
    while True:
        if player.hp <= 0:
            break
        choice = input(textwrap.dedent("""
            Menu
            0 - Go out to the fields and train
            1 - Check character status
            2 - Enter the castle! NOTE: I would advise saving at this point.
            3 - Use potion
            4 - Save. Please save often.
            5 - Quit Game
            """))
        if choice == "0":
            player = random_battle(player, inventory)
        elif choice == "1":
            player_status(player)
            delay = input("Press enter to continue...")
        elif choice == "2":
            #The choice you make alters storyline. Sorry its not really creative haha.
            print("As you reach the castle, you hear a mysterious voice. \"I can grant you power beyond your imagination. In return, I only ask of you to slay the Dragon King for me.\"")
            selection = input("You are curious yet hesitant and suspicious about this voice's offer. What do you do? Input 0 to accept and 1 to ignore the voice and venture forth.\n")
            if selection == "1":
                boss_battle(player,inventory)
            elif selection == "0":
                boss_battle2(player,inventory)
            break
        elif choice == "3":
            player.use_potion(inventory)
        elif choice == "4":
            save(player,inventory)
        elif choice == "5":
            print("Good Bye!")
            break

