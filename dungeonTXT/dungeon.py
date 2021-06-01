from riddles_secret import riddles, answers, sentences
from os import system, name
import random
import time

been_to_shrot_memory = False
been_to_boss = False
been_to_riddle = False
has_the_key = False
secret_sentence = sentences[random.randint(0, len(sentences) - 1)]
secret_words_list = secret_sentence.split()


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def has_key():
    return has_the_key


def hub():
    print("Insert the words, or continue with the directions\n")


def dull_room():
    dull_room_texts = ["Nothing special here(?)",
                       "Can you find the way?",
                       "Where you want to go next?",
                       "Some other ways here."]
    # Do random from this list and print to screen
    print(dull_room_texts[random.randint(0, len(dull_room_texts) - 1)])


def short_memory_room():
    global been_to_shrot_memory

    if not been_to_shrot_memory:
        print("""This is a shortmemory test room!
    For a brief moment a number will appear on screen.
    Your objective is to try to remembrer them!
    Are you ready? (yes/no)""")

        if input('\n> ').lower() == 'yes':
            pass
            clear()
        else:
            clear()
            print('May be next time')
            return

        shortmemory_test()

    else:
        print("You have already been here!")


def shortmemory_test():
    global been_to_shrot_memory, secret_words_list
    right_answers = 0
    sleep_time = 0.5

    for i in range(1, 6):  # Increasing number of numbers to memorize
        short_input = ''
        clear()
        for item in range(0, i):  # Printing random numbers for a breif moment
            short_numbers = random.randint(0, 99)
            print(short_numbers)
            short_input = short_input + str(short_numbers) + ' '
        time.sleep(sleep_time)
        sleep_time += 0.2

        clear()

        if input('> ') == short_input[: -1]:  # Checking user input before last char, because last char is ' '
            right_answers += 1

            if right_answers == 5:
                clear()
                print("Here is one of the words: " + secret_words_list[1])
                been_to_shrot_memory = True
                return
            else:
                print('Nice. Next sequence.')
                continue
                time.sleep(1)
                clear()

        else:
            print('wrong')
            return


def riddle_room():
    global been_to_riddle, has_the_key, riddles, answers

    if not been_to_riddle:
        print("Are you ready to give a word to receive a word? (yes/no)")
        wants_to = input('\n> ').lower()
        if wants_to == 'yes':
            pass
            clear()
        elif wants_to == 'no':
            clear()
            print('May be next time')
            return
        else:
            clear()
            print('Was it a typo? (try re-entering the room)')
            return

        riddle_number = random.randint(0, len(riddles) - 1)

        for i in range(0, 3):
            print("This is a Riddle:\n" + riddles[riddle_number])
            riddle_user_answer = input().lower()

            if riddle_user_answer == answers[riddle_number]:
                been_to_riddle = True
                has_the_key = True
                clear()
                print("Here, take the key and one word: " + secret_words_list[0])
                break
            else:
                clear()
                print(f"Answer is not correct, {2-i} tries left.\n")
                if i == 2:
                    clear()
                    print("You lose the game!\n")
                    exit(0)

    else:
        print("You have already been here!")


def boss():
    global been_to_boss, secret_words_list

    if not been_to_boss:
        print("Are you ready to have a fight with a boss? (yes/no)")
        wants_to = input('\n> ').lower()
        if wants_to == 'yes':
            clear()
            boss_fight()

        elif wants_to == 'no':
            clear()
            print('May be next time')
            return
        else:
            clear()
            print('Was it a typo? (try re-entering the room)')
            return

    else:
        print("You have already been here!")


def boss_fight():
    global been_to_boss
    shot = False
    magnum_mag = [0, 0, 0, 0, 0, 0]
    bullet_count = 0

    print("You are in the boss room and random will determine your luck!")
    print("Bring on the big guns and be ready to shuffle!")
    time.sleep(3)
    clear()
    print("We'll play a Russian Roulette")
    print("Take this magnum and shuffle while you can, after you shoot, you won't be able to shuffle anymore!")

    while not been_to_boss:
        shuffle_or_shoot = input()
        clear()

        if shuffle_or_shoot == 'shuffle':
            if shot:
                print("You've already shot, can't shuffle")
                pass
            else:
                magnum_mag = shuffle(magnum_mag)

        elif shuffle_or_shoot == 'shoot':
            shot = True
            bullet_count, been_to_boss = shoot(bullet_count, magnum_mag, been_to_boss)

        else:
            print("You had one job, shuffle or shoot!")
            exit(0)


def shuffle(magnum_mag):
    print("\nSHUFFLING\n")
    magnum_mag = [0, 0, 0, 0, 0, 0]
    magnum_mag[random.randint(0, len(magnum_mag) - 1)] = 1
    return magnum_mag


def shoot(bullet_count, magnum_mag, been_to_boss):
    global secret_words_list
    if magnum_mag[bullet_count] == 0:
        print('That was close!')
        print('Now I will try my luck!')
        bullet_count += 1
        time.sleep(0.8)
        clear()

        if magnum_mag[bullet_count] == 0:
            print('I am also UNDEFFITABLE')
            bullet_count += 1
            return bullet_count, been_to_boss
        else:
            print("How lucky Can you be? Oh, I'm dead, how can I be speaking right now?")
            print("OK, I will shut up now :deadbossnoises:\n\n\n")
            print("Oh, but before I go, here is my last word: " + secret_words_list[2])
            been_to_boss = True
            return bullet_count, been_to_boss
    else:
        print("Oh you pure creature, you can't even take a led bullet to your head without dying\n\n")
        exit(0)


# Call each dungeon by given coordinates


def dungeon_main(coordinates):
    if coordinates == [0, 0]:
        hub()
    elif coordinates == [1, 0]:
        dull_room()
    elif coordinates == [1, 1]:
        riddle_room()
    elif coordinates == [2, 0]:
        short_memory_room()
    elif coordinates == [-1, 0]:
        dull_room()
    elif coordinates == [0, -1]:
        dull_room()
    elif coordinates == [-1, -1]:
        boss()
    else:
        pass
