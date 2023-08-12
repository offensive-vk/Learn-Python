# Star Pattern
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)


# Number Pattern
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Diamond pattern
size = int(input("Enter the size of the diamond: "))
for i in range(size):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))
for i in range(size - 2, -1, -1):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))

# Number Pyramid
rows = int(input("Enter the number of rows: "))
num = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()
