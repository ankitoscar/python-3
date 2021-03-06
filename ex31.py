# Decision making in python
# Printing intialising message
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

# Taking input for number of doors
door = input(">")

# If statement block
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # Taking input of number of bears
    bear = input(">")

    # If statements inside if block
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

# Elif statements involving doors
elif door == "2":
    # Print messages
    print("You stare into the endless abyss at Cthulhu's retina")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    # Taking insanity input
    insanity = input(">")

    # If inside if
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    # Else statement
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

# Else statement
else:
    print("You stumble around and fall on a knife and die. Good job!")
