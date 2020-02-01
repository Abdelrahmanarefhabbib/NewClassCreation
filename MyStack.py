class MyStack:
    def __init__(self, max_size=float("inf")):
        self.stack = []
        self.max_size = max_size

    def push(self, new_data):
        if self.max_size > len(self.stack):
            self.stack.append(new_data)
        else:
            raise IndexError("Stack max size reached")

    def pop(self):
        return self.stack.pop()

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def get_size(self):
        return len(self.stack)
