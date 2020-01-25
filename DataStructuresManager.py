from MyAVLTree import MyAVLTree
from MyBinaryTree import MyBinaryTree
from MyHeap import MyHeap
from MyLinkedList import MyLinkedList
from MyQueue import MyQueue
from MyStack import MyStack
from MyTwoThreeTree import MyTwoThreeTree


class DataStructuresManager:
    def __init__(self):
        self.linked_lists = []
        self.queues = []
        self.stacks = []
        self.heaps = []
        self.binary_trees = []
        self.avl_trees = []
        self.two_three_trees = []

    def create_new_linked_list(self):
        self.linked_lists.append(MyLinkedList())

    def delete_linked_list(self, index=None):
        """ if no index is provided last element will be deleted"""
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
        """ if no index is provided last element will be deleted"""
        if index is None:
            self.queues.pop()
        else:
            self.queues.pop(index)

    def delete_all_queues(self):
        self.queues = []

    def create_new_stack(self, max_size=float("inf")):
        self.stacks.append(MyStack(max_size))

    def delete_stack(self, index=None):
        """ if no index is provided last element will be deleted"""
        if index is None:
            self.stacks.pop()
        else:
            self.stacks.pop(index)

    def delete_all_stacks(self):
        self.stacks = []

    def create_new_heap(self, max_size=float("inf")):
        self.heaps.append(MyHeap(max_size))

    def delete_heap(self, index=None):
        """ if no index is provided last element will be deleted"""
        if index is None:
            self.heaps.pop()
        else:
            self.heaps.pop(index)

    def delete_all_heaps(self):
        self.heaps = []

    def print_all_heaps(self):
        for heap in self.heaps:
            heap.print_heap()
            print

    def create_new_binary_tree(self):
        self.binary_trees.append(MyBinaryTree())

    def delete_binary_tree(self, index=None):
        """ if no index is provided last element will be deleted"""
        if index is None:
            self.binary_trees.pop()
        else:
            self.linked_lists.pop(index)

    def print_all_binary_trees(self):
        for binary_tree in self.binary_trees:
            binary_tree.print_tree()
            print

    def delete_all_binary_trees(self):
        self.binary_trees = []

    def search_all_binary_trees(self, key):
        for binary_tree in self.binary_trees:
            if binary_tree.search(key):
                return True
        return False

    def create_new_avl_tree(self):
        self.avl_trees.append(MyAVLTree())

    def delete_avl_tree(self, index=None):
        """ if no index is provided last element will be deleted"""
        if index is None:
            self.avl_trees.pop()
        else:
            self.avl_trees.pop(index)

    def print_all_avl_trees(self):
        for avl_tree in self.avl_trees:
            avl_tree.print_tree()
            print

    def delete_all_avl_trees(self):
        self.avl_trees = []

    def search_all_avl_trees(self, key):
        for avl_tree in self.avl_trees:
            if avl_tree.search(key):
                return True
        return False

    def create_new_two_three_tree(self):
        self.two_three_trees.append(MyTwoThreeTree())

    def delete_two_three_tree(self, index=None):
        """ if no index is provided last element will be deleted"""
        if index is None:
            self.two_three_trees.pop()
        else:
            self.two_three_trees.pop(index)

    def print_all_two_three_trees(self):
        for two_three_tree in self.two_three_trees:
            two_three_tree.print_tree()
            print

    def delete_all_two_three_trees(self):
        self.two_three_trees = []

    def search_all_two_three_trees(self, key):
        for two_three_tree in self.two_three_trees:
            if two_three_tree.search(key):
                return True
        return False
