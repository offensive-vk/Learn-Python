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


# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())  # Output: 3

print(stack.pop())   # Output: 3
print(stack.pop())   # Output: 2
print(stack.pop())   # Output: 1

print(stack.isEmpty())  # Output: True