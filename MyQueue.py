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
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Front from empty queue")

    def rear(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            raise IndexError("Rear from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def get_size(self):
        return len(self.queue)
