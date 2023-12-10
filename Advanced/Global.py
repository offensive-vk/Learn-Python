class Global:
    def __init__(self, name, age, salary):
        self.name = name
        self.salary = salary
        self.age = age

    def DisplayData(self, obj) -> str:
        print(f"Name : {obj.name}")
        print(f"Age : {obj.age}")
        print(f"Salary : {obj.salary}")

        return obj

## Usage
G = Global('Manish Pandey', 95000, 30)
G.displayData(G)