# Copying content from one file to another
# Importing packages
from sys import argv
from os.path import exists

# Passing arguments
script, from_file, to_file = argv

# Message for copying
print(f"Copying from {from_file} to {to_file}")

# Opening and reading the from_file
in_file = open(from_file)
indata = in_file.read()

# Printing lenght of file
print(f"The input file is {len(indata)} bytes long")

# Checking existence of to_file
print(f"Does the output file exists? {exists(to_file)}")
print("Ready for action, hit ENTER to continue, CTRL-C to abort")

# Taking input for futher action
input()

# Opening to_file
out_file = open(to_file, 'w')
out_file.write(indata)

# Printing end message
print("Achievement Unlocked, Task Completed!")

# CLosing the files
out_file.close()
in_file.close()
