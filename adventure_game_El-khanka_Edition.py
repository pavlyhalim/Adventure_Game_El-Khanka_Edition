
import time
import random

items = []

weapon = ['M416', 'DP28', 'MK14']
monster = ['Adly', 'David', 'Basel', 'Osama', 'Soudy']


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("Welcome adventurer!")
    name = input("What is your name ?\n")
    if not name:
        return intro()
    else:
        return intro2(name)


def intro2(name):
    weapon_this_game = random.choice(weapon)
    monster_this_game = random.choice(monster)
    items.clear()
    print_pause("\nYou have been chosen, {}, "
                "to save El Khanka.".format(name))
    print_pause("Dark forces are everywhere and "
                "you, {}, are our only hope!".format(name))
    print_pause("Your mission is to find "
                "{} and kill {} in "
                "a dark dungeon!".format(weapon_this_game, monster_this_game))
    print_pause("\nAfter drinking a magic poti, you find"
                " yourself in the dark dungeon.")
    door_choice(name, weapon_this_game, monster_this_game)


def first_door(name, weapon_this_game, monster_this_game):
    print_pause("\nYou enter the bedroom.")
    if weapon_this_game in items:
        print_pause("The ghost appear again "
                    "and start talking to you.")
        print_pause("Sorry, {}, I already gave you the {} to defeat the "
                    "{}.".format(name, weapon_this_game, monster_this_game))
        print_pause("You thank him again and leave the room.")
        door_choice(name, weapon_this_game, monster_this_game)
    else:
        print_pause("A ghost appear in front of you "
                    "and start talking to you.")
        print_pause("Hello, {}, I was waiting for you.".format(name))
        print_pause("Someone told me you will need "
                    "this to defeat the {}.".format(monster_this_game))
        print_pause("The ghost make appear the {} "
                    "and give it to you.".format(weapon_this_game))
        print_pause("You thank him and leave the room.")
        items.append(weapon_this_game)
        door_choice(name, weapon_this_game, monster_this_game)


def second_door(name, weapon_this_game, monster_this_game):
    print_pause("\nYou enter the bathroom.")
    print_pause("This is the {}'s lair!".format(monster_this_game))
    choice_fight(name, weapon_this_game, monster_this_game)
    if weapon_this_game in items:
        print_pause("\nThe {} attacks you as soon "
                    "as you pass the door!".format(monster_this_game))
        if weapon_this_game == 'DB28':
            print_pause("You do your best...")
            print_pause("but you realize your {}"
                        " is just a carrot!".format(weapon_this_game))
            print_pause("Too late!")
            print_pause("You have been defeated.")
            play_again(name)
        else:
            print_pause("After an epic fight, you defeat "
                        "{}, thanks to "
                        "{}!".format(monster_this_game, weapon_this_game))
            print_pause("\nCongratulations! You save El Khanka!")
            play_again(name)
    else:
        print_pause("\nAre you sure you want to fight the {} without "
                    "the {}?".format(monster_this_game, weapon_this_game))
        choice_fight(name, weapon_this_game, monster_this_game)
        print_pause("\nThe {} attacks you as soon "
                    "as you pass the door!".format(monster_this_game))
        print_pause("You do your best...")
        print_pause("but without the {}, the {}"
                    " win easily!".format(weapon_this_game, monster_this_game))
        print_pause("You have been defeated.")
        play_again(name)


def choice_fight(name, weapon_this_game, monster_this_game):
    fight_or_not = input("\nWould you like to (1) fight or (2) "
                         "go back to the door choice?\n")
    if fight_or_not == '1':
        return True
    elif fight_or_not == '2':
        door_choice(name, weapon_this_game, monster_this_game)
    else:
        print_pause("Please {}, enter 1 or 2!\n".format(name))
        choice_fight(name, weapon_this_game, monster_this_game)


def door_choice(name, weapon_this_game, monster_this_game):
    print_pause("\nIn front of you are two doors.\n")
    door = input("Enter 1 to enter the first door.\n"
                 "Enter 2 to enter the second door.\n"
                 "What door do you want to open ?\n")
    if door == '1':
        first_door(name, weapon_this_game, monster_this_game)
    elif door == '2':
        second_door(name, weapon_this_game, monster_this_game)
    else:
        print_pause("Please {}, enter 1 or 2!\n".format(name))
        door_choice(name, weapon_this_game, monster_this_game)


def play_again(name):
    choice_again = input("\nWould you like to play again ?"
                         " Please say 'yes' or 'no'.\n").lower()
    if 'no' in choice_again:
        print_pause("\nOk, Goodbye {}.".format(name))

    elif 'yes' in choice_again:
        print_pause("\nExcellent {}, restarting the game ...".format(name))
        intro2(name)
    else:
        print_pause("Please {}, enter 'y' or 'n'!".format(name))
        play_again(name)


intro()
