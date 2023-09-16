
class Sourabh:
    name = ''
    counter = 0
    marks = int(0)
    def __init__(self):
        self.counter += 1
        pass
    def __init__(self, _name) -> None:
        self.name = _name
        print(f"Constructor of {self.name} Class has been created. ")
        self.counter += 1
        pass
    def calculate():
        return "Calculating ..."
    def count(self):
        print(f"Number of Objects Created : {self.counter}")
        
# top = Sourabh('')
# # top.mark(966)

# first = Sourabh("Manish")
# second = Sourabh("Rupesh")
# third = Sourabh("Himanshu")

# top.count()


class doSomething(Sourabh):
    # def __init__(self, _name) -> None:
    #     super().__init__(_name)
    def __init__(self) -> None:
        print("doSomething called ")
        
        
    def add()->None:
        print('You havent entered something')
        return None
    def add(a,b)-> int:
        return a + b
    def add(a,b,c)-> int:
        return a + b + c
    def add(a, b, c, d)-> int:
        return a + b + c + d
    
do = doSomething()
do.calculate()