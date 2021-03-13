# Program involving explictly overriding in inheritance
class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent() # Parent class instance
son = Child() # Child class instance

dad.override()
son.override()
