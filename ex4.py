# Initializing number of cars
cars = 100

# Initializing space in cars
space_in_a_car = 4.0

# Number of drivers
drivers = 30

# Number of passengers
passengers = 90

# Initializing variables with operations
# Number of cars not driven
cars_not_driven = cars - drivers

# Number of cars driven
cars_driven = drivers

# Carpool capacity
carpool_capacity = cars_driven * space_in_a_car

# Average passengers
average_passengers = passengers / cars_driven

# Print all these variables
# Printing available cars
print("There are", cars, "cars available")

# Printing number of drivers available
print("There are only", drivers, "drivers available")

# Printing number of empty drivers
print("There will be", cars_not_driven, "empty cars today")

# Printing total people who can be transported today
print("We can transport", carpool_capacity, "people today.")

# Printing number of passengers for today
print("We have", passengers,"to carpool today.")

# Printing number of average passengers in a car 
print("We need to put about", average_passengers, "in each car.")
