def greet(name):
    return " Hello !", name


def num(num):
    return num * 2


class Number:
    number = 0
    res = 0

    def __init__(self, number):
        self.number = number
        res = number * number + number
        print("Number: ", res)
