# Accessing files with functions
# Importing argv
from sys import argv

# Passing arguments to argv
script, input_file = argv

# Writing functions
# Function to print all text in file
def print_all(f):
    print(f.read())

# Not sure what this does
def rewind(f):
    f.seek(0)

# Print first line of a file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Reading the file to be worked upon
current_file = open(input_file)

# Printing the whole file
print_all(current_file)

# Rewinding.....
rewind(current_file)

# Printing three lines
current_line = 1

# Printing line 1
print_a_line(current_line, current_file)

# Printing line 2
current_line += 1
print_a_line(current_line, current_file)

# Priting line 3
current_line += 1
print_a_line(current_line, current_file)
