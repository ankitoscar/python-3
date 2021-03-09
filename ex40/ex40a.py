# import mystuff modules
import mystuff

# calling apple for module
mystuff.apple()

# importing tangerine from module
print(mystuff.tangerine)

# making a class named 'MyStuff'
class MyStuff(object):

    # constructor
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    # apple
    def apple(self):
        print("I AM CLASSY APPLES!")

# making an object
thing = MyStuff()
thing.apple()
print(thing.tangerine)
