class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None

    def isEmpty(self):
        return len(self.stack) == 0


