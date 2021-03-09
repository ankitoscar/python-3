# Program involving use of lists
# Initialising a list
ten_things = "Apples Oranges Crows Telephones Light Sugar"

# Printing the message that 'ten_things' doesn't have 10 things
print("Wait there are not 10 things in that list. Let's fix that.")

# Splitting ten_things
stuff = ten_things.split(' ') # split() splits a string on seeing the passed character

# Initialising a list called 'more_stuff'
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Core', 'Banana', 'Girl', 'Boy']

# Appending items from more_stuff to ten_things using while loop
while len(stuff) != 10:
    next_one = more_stuff.pop() # Pops out last element of more_stuff
    print("Adding: ", next_one) # Printing the message to add next_one to stuff
    stuff.append(next_one) # Appending next_one to stuff
    print(f"There are {len(stuff)} items now.") # Showing no. of items in stuff at present

# Showing stuff and the 10 elements in it
print("There we go: ", stuff)

# Crazy thing with stuff
print("Let\'s do some things with stuff.")

# Crazy things begins
print(stuff[1])
print(stuff[-1]) # Gives last element of stuff
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5])) # Shows 4th to 5th element of stuff, also called slicing 
