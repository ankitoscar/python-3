# Program containing elif and else statements
# Initialising variables
people = 30
cars = 40
trucks = 15

# if, else and elif statements
if cars > people:
    print("We should take the cars.")

elif cars < people:
    print("We should not take the cars.")

else:
    print("We can't decide.")

# More if, else and elif statements
if trucks > cars:
    print("That's too many trucks.")

elif trucks < cars:
    print("Maybe we could take the trucks,")

else:
    print("We still can't decide.")

# Just last statements
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
