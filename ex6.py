# Formatted strings
# Number of types of people
types_of_people = 10
x = f"There are {types_of_people} types of people."

# People who know binary and people who don't
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Printing x and y
print(x)
print(y)

# Printing more statements
print(f"I said {x}.")
print(f"I also said : '{y}'")

# Initialising more variables
hilarous = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Another formatted string
print(joke_evaluation.format(hilarous))

# Some more string variables
w = "This is the left side of ..."
e = "a string with a right side."

# Printing w + e
print(w + e)
