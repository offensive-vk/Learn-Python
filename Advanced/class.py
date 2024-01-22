# a class is a blueprint for creating objects. Objects are instances of classes, 
# and classes define the properties (attributes) and behaviors (methods) that the objects created from them will have. 

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an instance of the Dog class
my_dog = Dog(name="Buddy", age=3)

# Accessing attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling a method
my_dog.bark()