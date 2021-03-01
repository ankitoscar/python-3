# Some more functions
# Function for cheese and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("That's enough for a party")
    print("Get a blanket.\n")

# Calling above function by passing numbers
print("We can just call the function by passing numbers")
cheese_and_crackers(20,30)

# Passing variable to the cheese_and_crackers function
print(f"Using variables in the script")
amount_of_cheese = 10
amount_of_crackers = 40

# Calling the function by passing above arguments
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# Passing math operations between numbers as arguments
cheese_and_crackers(10 + 5 - 1, 20 / 5 + 2)

# Combining math and variables
print("Combining math and variables")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers - 20)
