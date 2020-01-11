class MyQueue:
    def __init__(self, max_size=float("inf")):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, new_data):
        if self.max_size > len(self.queue):
            self.queue.append(new_data)
        else:
            raise IndexError("Queue max size reached")

    def dequeue(self):
        self.queue.pop(0)

    def front(self):
        if len(self.queue) != 0:
            return self.queue[0]
        return

    def rear(self):
        if not self.is_empty():
            return self.queue[len(self.queue) - 1]
        return

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def get_length(self):
        return len(self.queue)