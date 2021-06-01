from functions import *
from dungeon import dungeon_main, secret_sentence, clear

clear()

print("""\t\t\tHello and welcome!\n
You are now in the HUB!\n
Your objective is to get all 3 words from this dungeon
and make a sentence. Return to the HUB and check if the
sentence is right

type help, for help :D
""")


def start():
    global secret_sentence
    coordinates = [0, 0]
    move_commands = ['north', 'east', 'south', 'west']
    moved = False
    not_blocked = False

    while True:
        user_input = input("\n> ").lower()
        clear()

        if user_input in move_commands:
            coordinates, moved, not_blocked = update_coordinates(user_input, coordinates)
            if moved and not_blocked:
                dungeon_main(coordinates)
            elif not moved and not not_blocked:
                print("You need a key!")
            else:
                print(f"There are no ways in {user_input}")
                pass

        elif user_input == secret_sentence and coordinates == [0, 0]:
            clear()
            print("YOU WIN\n")
            exit(0)

        elif user_input == 'help':
            f = open('help.txt')
            print(f.read())
            f.close()

        elif user_input == 'quit':
            exit(0)

        else:
            print('Unknown Command')

        print("\n" * 5, coordinates, " <-- Current position")


start()
