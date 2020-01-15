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
            index = len(self.heap) - 1
            while index != 0 and self.heap[get_parent_index(index)] > self.heap[index]:
                swap_position(self.heap, index, get_parent_index(index))
                index = get_parent_index(index)

    def pop(self, pos):
        self.heap[pos] = self.heap[-1]
        deleted_value = self.heap.pop()
        if pos < len(self.heap):
            self.shift_up(pos)
            self.shift_down(pos)

        return deleted_value

    def is_full(self):
        return len(self.heap) == self.max_size

    def is_empty(self):
        return len(self.heap) == 0

    def print_heap(self):
        for element in self.heap:
            print element,

    def shift_up(self, pos):
        data_to_shift = self.heap[pos]
        current_pos = pos

        while current_pos > 0:
            parent_pos = (current_pos / 2) + 1
            if data_to_shift < self.heap[parent_pos]:
                self.heap[current_pos] = self.heap[parent_pos]
                current_pos = parent_pos
            else:
                break
        self.heap[pos] = data_to_shift

    def shift_down(self, pos):
        data_to_shift = self.heap[pos]
        child_pos = 2*pos + 1

        while child_pos < len(self.heap):
            right_child = child_pos + 1
            if right_child < len(self.heap) and self.heap[child_pos] > self.heap[right_child]:
                child_pos = right_child
            if data_to_shift > self.heap[child_pos]:
                self.heap[pos] = self.heap[child_pos]
            else:
                break
            pos = child_pos
            child_pos = 2*pos + 1
        self.heap[pos] = data_to_shift

    def get_min(self):
        return self.heap[0]


def get_parent_index(index):
    return (index-1)/2


def swap_position(my_list, pos1, pos2):
    my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]