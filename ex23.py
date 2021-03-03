# Importing sys for taking arguments in argv
import sys

# Passing arguments to argv
script, input_encoding, error = sys.argv

# Function for reading the languages file
def main(language_file, encoding, errors):
    line = language_file.readline() # reading line from language_file
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # Recursion

# Function to print a line
def print_line(line, encoding, errors):
    next_lang = line.strip() # Removing extra spaces
    raw_bytes = next_lang.encode(encoding, errors = errors) # Converting string to bytes
    cooked_string = raw_bytes.decode(encoding, errors = errors) # Converting bytes to string

    print(raw_bytes, "<===>", cooked_string)

# Loading the language_file
languages = open("languages.txt", encoding = "utf-8")

# Calling the main() function
main(languages, input_encoding, error)
