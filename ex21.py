# Making functions which return some value
# Mainly Mathematical functions
# Function to add two numbers
def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    print(f"Subtracting {a} and {b}")
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    print(f"Multiplying {a} and {b}")
    return a * b

# Function to divide two numbers
def divide(a, b):
    print(f"Dividing {a} and {b}")
    return a / b

# Doing some math with these functions
print("Doing some math....")

# Calling functions
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# Priting all variables
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# Some crazy statement
print("Puzzle time.....")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# Printing the 'what' variable
print(f"That becomes: {what}\nCan you do it by hand?")
