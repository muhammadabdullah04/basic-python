# Stack class 
class Stack:
    def __init__(self):
        self.container = []

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def reverse_string(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)

    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

print(reverse_string("We will conquere COVID-19"))
