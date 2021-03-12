# Program showing is-a and has-a relation between classes and objects
## Animal is an object
class Animal(object):
    pass

## Dog is an animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is also an animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name 
        self.name = name

## Person is an object
class Person(object):

    def __init__(self, name):
        ## Constuctor
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        ## Taking name for this constructor and passing as name of Person class
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## Salmon is a fish
class Salmon(Fish):
    pass

## Halibut is also a fish
class Halibut(Fish):
    pass

## rover is-a dog '
rover = Dog("Rover")

## Satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## Satan is Mary's pet
mary.pet = satan

## Frank is an Employee
frank = Employee("Frank", 120000)

## Rover is-a pet of Frank
frank.pet = rover

## Flipper is-a fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
