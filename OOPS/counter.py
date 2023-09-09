class MyClass:
    # Class variable to keep track of the number of objects created
    num_objects = 0

    def _init_(self):
        # Increment the count of objects when a new object is created
        MyClass.num_objects += 1

    @staticmethod
    def get_num_objects():
        return MyClass.num_objects

# Create some objects of the class
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

# Print the number of objects created
print("Number of objects created:", MyClass.get_num_objects())