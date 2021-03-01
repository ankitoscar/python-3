# Importing argv
from sys import argv

# Taking script and filename as arguments
script, filename = argv

# Printing file erase message
print(f"We're are going to erase {filename}.")
# Asking user whether they want to erase the file or not
print("If you don't want to do that, hit Ctrl + C (^C).")
print("If you don't want that, press Return/Enter")

input("?")

# Opening the file with message
print("Opening the file.....")
target = open(filename,'w')

# Erasing the file
print("Truncating the file, sed.")
target.truncate()

# Asking user to give files for writing
print("Now, I'm going to ask you for three lines")

# Taking lines from user
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Message for writing all three lines
print("Now I'm going to write all three lines")

# Writing all three lines
target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

# Closing message
print("And finally we close it.")

# Closing the files
target.close()
