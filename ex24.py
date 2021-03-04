# Practicing everything learned till now
# Message showing we are going to practice everything
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# Writing a poem
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# Printing the poem
print("-------------")
print(poem)
print("-------------")

# Making a math exp which is equal to 5
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# Function for a secret formula
def secret_function(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# Making a start point for secret_function
start_point = 10000
beans, jars, crates = secret_function(start_point)

# Printing secret_function output
print("With starting point of: {}".format(start_point)) # Another way of formatting strings
print(f"We'd have {beans} beans, {jars} jars and {crates} crates.")

# reducing start_point by * 10
start_point = start_point / 10

# Alternative
print("We can also do that this way:")
formula = secret_function(start_point)
# Formatting string with members of list
print("We'd have {} beans, {} jars and {} crates".format(*formula))
