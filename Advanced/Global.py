from abc import abstractmethod
class Top:
    def __init_subclass__(cls, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def display(self):
        pass

class Global:
    def __init__(self, name, age, salary):
        self.name = name
        self.salary = salary
        self.age = age

    @staticmethod
    def displayData(obj) -> str:
        print(f"Name : {obj.name}")
        print(f"Age : {obj.age}")
        print(f"Salary : {obj.salary}")
        return obj

    @staticmethod
    def updateData(obj) -> str:
        print("What Do you wanna update? \n")
        print(f"1. Name : (Current Set : {obj.name})")
        print(f"2. Age : (Current Set : {obj.age})")
        print(f"3. Salary : (Current Set : {obj.salary})")
        print(f"4. Nothing (Exit)")
        choice = int(input("Choose An Option [1/2/3] : "))
        if choice == 1:
            obj.name = input("Re-Enter Your Name (New): ")
            print(f"Updated Name To {obj.name}\n")
        if choice == 2:
            obj.age = input("Re-Enter Your Age (New): ")
            print(f"Updated Age To {obj.age}\n")
        if choice == 3:
            obj.salary = input("Re-Enter Your Salary (New): ")
            print(f"Updated Salary To {obj.salary}\n")
        if choice == 4:
            print(f" Updated : NULL (Exit)\n")
        else:
            print(f"Invalid Choice / Out of Options. ")
            pass
        return obj

# Usage
G = Global('Alex', 95000, 30)
R = Global("Raju", 55, 65000)

print(f"Showing {G.name}'s data : \n")
Global.displayData(G)

print("=========================\n")

print(f"Showing {R.name}'s data : \n")
Global.displayData(R)
print("=========================\n")
