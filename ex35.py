# Program involving if statements and functions
# Importing exit() from sys
from sys import exit

# Defining gold_room()
def gold_room():
    # Printing initial message
    print("This room is full of gold. How much do you take?")

    # Taking user input
    choice = input(">")
    # If statement
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    # Another if statement
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

# Defining bear_room()
def bear_room():
    # Printing initial message
    print("""
    There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?
    """)
    bear_moved = False

    # While loop
    while True:
        # Taking input from user
        choice = input(">")

        # If statements
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your legs off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

# Defining cthulhu_room()
def cthulhu_room():
    # Printing initial message
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    # Taking user input
    choice = input(">")

    # If statements
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

# Defining dead()
def dead(why):
    # initial message
    print(why, "Good job!")
    exit(0)

# Defining start()
def start():
    # Printing initial message
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    # Taking user input
    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
