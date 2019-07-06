class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size():
            val = self.stack[0]
            self.stack = self.stack[1:]
            return val
        return None

    def push(self, value):
        self.stack = [value] + self.stack

    def peek(self):
        if self.size():
            return self.stack[0]
        return None
