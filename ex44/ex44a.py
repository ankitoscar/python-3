# Program involving implicit inheritance
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent() # Parent class instance
son = Child() # Child class instance

dad.implicit()
son.implicit()
