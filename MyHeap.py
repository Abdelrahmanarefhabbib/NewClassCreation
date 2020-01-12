class MyHeap:
    """In this implementation the heap is a min heap"""
    def __init__(self, max_size=float("inf")):
        self.heap = []
        self.max_size = max_size

    def push(self, new_data):
        if self.is_full():
            raise IndexError("Heap max size reached")
        else:
            self.heap.append(new_data)
            index = len(self.heap)

            while index != 0 and self.heap[self.get_parent_index(index)] > self.heap[index]:
                self.swap_position(index, self.get_parent_index(index))
                index = self.get_parent_index(index)

    @property
    def get_parent_index(i):
        return (i-1)/2

    def swap_position(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def is_full(self):
        return len(self.heap) == self.max_size

    def is_empty(self):
        return len(self.heap) == 0
