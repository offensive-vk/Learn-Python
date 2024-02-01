import os

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


x, y = 0, 0
while True:
    print("\n======================\n")
    print("-> Welcome To Calculator <- \n")
    print("1. Addition \n")
    print("2. Subtraction \n")
    print("3. Multiplication \n")
    print("4. Division \n")
    print("5. Exit \n")
    print("\t=======================\n")
    choice = input(" -> Choose Your Option : ")
    if choice == '1' or choice == 'add':
        x = int(input(" -> Enter X : "))
        y = int(input(" -> Enter Y : "))
        print(f"-> Addition of {x} and {y} is : {add(x, y)}")
        break
    elif choice == '2' or choice == 'sub':
        x = int(input(" -> Enter X : "))
        y = int(input(" -> Enter Y : "))
        print(f"-> Subtraction of {x} and {y} is : {sub(x, y)}")
        break
    elif choice == '3' or choice == 'mul':
        x = int(input(" -> Enter X : "))
        y = int(input(" -> Enter Y : "))
        print(f"-> Multiplication of {x} and {y} is : {mul(x, y)}")
        break
    elif choice == '4' or choice == 'div':
        x = int(input(" -> Enter X : "))
        y = int(input(" -> Enter Y : "))
        print(f"-> Division of {x} and {y} is : {div(x, y)}")
        break
    elif choice == '5' or choice == 'exit':
        os.system("cls")
        print("Thanks for using Calculator, Goodbye !\n")
        break
    else:
        print(f" -> You Have Selected Invalid Option ! Please Try Again. \n")
        continue
