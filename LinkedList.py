from Node import Node


class LinkedList:
    def __init__(self):
        self.root_value = None

    def add_node(self, new_data):
        if self.root_value is None:
            self.root_value = Node(new_data)
            return

        current_node = self.root_value
        while current_node.next_value:
            current_node = current_node.next_value
        current_node.next_value = Node(new_data)

    def remove_node(self, remove_key):
        current_node = self.root_value
        if current_node is not None:
            if current_node.data == remove_key:
                self.root_value = current_node.next_value
                current_node = None
                return

        while current_node is not None:
            if current_node.data == remove_key:
                break
            prev_node = current_node
            current_node = current_node.next_value

        if current_node is None:
            return

        prev_node.next_value = current_node.next_value
        current_node = None

    def print_list(self):
        print_value = self.root_value
        while print_value is not None:
            print (print_value.data_value)
            print_value = print_value.next_value
