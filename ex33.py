# Program involving while loop
i = 0

# Initialising empty list
numbers = []

# While loop
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i) # Appending i to numbers

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

# Printing elements of number
print("The numbers: ")

# For loop
for num in numbers:
    print(num)
