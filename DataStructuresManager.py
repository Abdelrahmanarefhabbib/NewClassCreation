from MyLinkedList import MyLinkedList
from MyQueue import MyQueue
from MyStack import MyStack


class DataStructuresManager:
    def __init__(self):
        self.linked_lists = []
        self.queues = []
        self.stacks = []

    def create_new_linked_list(self):
        self.linked_lists.append(MyLinkedList())

    def delete_linked_list(self, index=None):
        """ if no index is provided last linked list will be deleted"""
        if index is None:
            self.linked_lists.pop()
        else:
            self.linked_lists.pop(index)

    def print_all_linked_lists(self):
        for linked_list in self.linked_lists:
            linked_list.print_list()
            print

    def delete_all_linked_lists(self):
        self.linked_lists = []

    def create_new_queue(self, max_size=float("inf")):
        self.queues.append(MyQueue(max_size))

    def delete_queue(self, index=None):
        """ if no index is provided last queue will be deleted"""
        if index is None:
            self.queues.pop()
        else:
            self.queues.pop(index)

    def delete_all_queues(self):
        self.queues = []

    def create_new_stack(self, max_size=float("inf")):
        self.queues.append(MyStack(max_size))

    def delete_stack(self, index=None):
        """ if no index is provided last queue will be deleted"""
        if index is None:
            self.stacks.pop()
        else:
            self.stacks.pop(index)

    def delete_all_stacks(self):
        self.stacks = []
