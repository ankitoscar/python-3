# Introduction to functions
# Function for printing two arguments
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Function for printing two arguments, again
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# Function for printing only one argument
def print_one(arg):
    print(f"arg: {arg}")

# Function which prints without any argument
def just_print():
    print("Just.. Nothing.")

# Calling all three functions
print_two("Conor","McGregor")
print_two_again("Dublin","Ireland")
print_one("The Notorious")
just_print()
