import export

name = input("Enter your name: ")
greeting = export.greet(name)
print(greeting)

num = int(input("Enter a number: "))
result = export.num(num)
print("Square:", result)

export.number = export.Number(749)
