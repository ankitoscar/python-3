# This exercise involves making a module and importing it in shell
# Various Functions

def break_words(stuff):
    """
    This function will break up words for us.
    """
    words = stuff.split(' ') # Splitting words seperated by ' ' into different variables
    return words

def sort_words(words):
    """
    Sorts the words in lexicographic order.
    """
    return sorted(words) # Sorted list of words

def print_first_word(words):
    """
    Prints the first word after popping it.
    """
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """
    Prints the last word after popping it.
    """
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """
    Takes in a full sentence and returns the words in sorted order.
    """
    words = break_words(sentence) # Seperating words in a sentence
    return sort_words(words) # Return list of sorted words

def print_first_and_last(sentence):
    """
    Prints the first and last word of sentence.
    """
    words = break_words(sentence) # Seperating words in a sentence
    print_first_word(words) # Printing first word
    print_last_word(words) # Printig last word

def print_first_and_last_sorted(sentence):
    """
    Prints the first and last word of a sorted sentence
    """
    words = sort_sentence(sentence) # Sorting words of a sentence after sorting
    print_first_word(words)
    print_last_word(words)
