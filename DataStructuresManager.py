from MyLinkedList import MyLinkedList


class DataStructuresManager:
    def __init__(self):
        self.linked_lists = []

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