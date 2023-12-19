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
