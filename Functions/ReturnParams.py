def sayHello() -> str :
    return "Hello !"

def showFee(name: str) -> int :
    print("Fees of {name} is ")
    return 70000*12

print(showFee("username"))
print(sayHello())