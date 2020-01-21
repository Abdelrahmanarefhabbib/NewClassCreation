from MyNode import MyNode


class MyLinkedList:
    def __init__(self):
        self.root = None

    def add_node(self, new_data):
        if self.root is None:
            self.root = MyNode(new_data)

        else:
            current_node = self.root
            while current_node.next_value:
                current_node = current_node.next_value
            current_node.next_value = MyNode(new_data)

    def remove_node_by_key(self, remove_key):
        if self.root is None:
            return

        current_node = self.root
        if current_node.data_value == remove_key:
            self.root = current_node.next_value
            return

        while current_node is not None:
            if current_node.data_value == remove_key:
                break
            prev_node = current_node
            current_node = current_node.next_value

        prev_node.next_value = current_node.next_value

    def print_list(self):
        print_value = self.root
        while print_value is not None:
            print print_value.data_value,
            print_value = print_value.next_value

    def remove_node_by_index(self, remove_index):
        current_node = self.root
        if remove_index == 0:
            self.root = current_node.next_value
            return

        for index in range(remove_index):
            if current_node is None:
                return
            prev_node = current_node
            current_node = current_node.next_value
        prev_node.next_value = current_node.next_value

    def remove_last_node(self):
        current_node = self.root
        while current_node.next_value is not None:
            prev_node = current_node
            current_node = current_node.next_value
        prev_node.next_value = None
