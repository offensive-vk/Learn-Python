"""
"Dunder" is short for "double underscore," and in Python, dunder methods are special methods that have double underscores at the beginning and end of their names. These methods are also known as magic methods or special methods. They play a crucial role in defining how objects of a class behave in various contexts. Dunder methods are invoked by the Python interpreter in response to specific operations on objects.

Here are some common dunder methods and their purposes:

__init__(self, ...): Initializes a newly created object. It is called when an object is created.

__repr__(self): Returns a string representation of the object that, when passed to the eval function, should recreate the object.

__str__(self): Returns a human-readable string representation of the object. It is called by the built-in str() function and print().

__len__(self): Returns the length of the object. It is called by the built-in len() function.

__add__(self, other): Defines behavior for the addition operator +.

__sub__(self, other): Defines behavior for the subtraction operator -.

__eq__(self, other): Defines behavior for the equality operator ==.

__lt__(self, other): Defines behavior for the less-than operator <.

__gt__(self, other): Defines behavior for the greater-than operator >.

__iter__(self): Returns an iterator object. It is required for an object to be iterable.

__next__(self): Returns the next value from an iterator. It is used in conjunction with __iter__ for iteration.

__enter__(self), __exit__(self, exc_type, exc_value, traceback): Used for context management with the with statement.

__call__(self, ...): Allows an object to be called like a function.
"""

class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"Object initialized with name: {self.name}")

    def __repr__(self):
        return f"MyClass(name={self.name})"

    def __str__(self):
        return f"This is an instance of MyClass with name: {self.name}"

    def __add__(self, other):
        if isinstance(other, MyClass):
            return MyClass(name=f"{self.name}_{other.name}")
        else:
            raise TypeError("Unsupported operand type for +: MyClass and {type(other)}")

    def __len__(self):
        return len(self.name)

    def __init_subclass__(cls, **kwargs):
        print(f"Subclass {cls.__name__} is being created.")

# Creating an instance of MyClass
obj1 = MyClass("Object1")

# Using the __repr__ and __str__ methods
print("Using __repr__:", repr(obj1))
print("Using __str__:", str(obj1))

# Using the __add__ method
obj2 = MyClass("Object2")
combined_obj = obj1 + obj2
print("Combined object:", combined_obj)

# Using the __len__ method
print("Length of obj1:", len(obj1))

# Creating a subclass
class MySubclass(MyClass):
    pass

# Output will show that the subclass is being created due to __init_subclass__