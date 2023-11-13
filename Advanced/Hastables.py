class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key '{key}' not found in the hashtable")

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next
        raise KeyError(f"Key '{key}' not found in the hashtable")

    def display(self):
        for i in range(self.size):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next
            print("None")


