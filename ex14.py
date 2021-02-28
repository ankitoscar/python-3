# Using argv and input to taking inputs from the users
# Importing sys
from sys import argv

# Taking arguments
script, user_name = argv
# Prompt message
prompt = ">"

# Initial message
print(f"Hello {user_name}, {script} script here!")
print(f"So {user_name}, do you like me?")
like = input(prompt)

# Asking user job
print(f"{user_name}, what do you do for a living?")
job = input(prompt)

# Printing all inputs
print(f"""
Alright, so {user_name} said {like} about liking me.
You are a {job} by profession, not sure how you do it.
Nice.
""")
