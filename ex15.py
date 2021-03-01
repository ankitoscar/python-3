# Import argv
from sys import argv

# Passing arguments
script, filename = argv

# Opening the txt file
txt = open(filename)

# Printing post import message
print(f"Here's your file {filename}.")
print(txt.read())
txt.close()

# Opening the same file again, for no reason
# Prompt
print("Type the filename again:")
file_again = input(">")

# Opening the file again
txt_again = open(file_again) # Maybe used for opening file without passing as argument

print(txt_again.read())

txt_again.close()
