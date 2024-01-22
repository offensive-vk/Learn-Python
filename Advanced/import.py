import Export

name = input("Enter your name: ")
greeting = Export.greet(name)
print(greeting)

num = int(input("Enter a number: "))
result = Export.num(num)
print("Square:", result)

Export.number = Export.Number(749)