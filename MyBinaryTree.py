from MyTreeNode import MyTreeNode


class MyBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, new_data):
        if self.root is None:
            self.root = MyTreeNode(new_data)

        else:
            if self.root.data_value < new_data:
                if self.root.right is None:
                    self.root.right = MyTreeNode(new_data)
                else:
                    linked_insert(self.root.right, new_data)
            else:
                if self.root.left is None:
                    self.root.left = MyTreeNode(new_data)
                else:
                    linked_insert(self.root.left, new_data)

    def print_tree(self):
        pre_order_print(self.root)

    def search(self, key):
        pre_order_search(self, key)


def linked_insert(current_node, new_data):
    if current_node.data_value < new_data:
        if current_node.right is None:
            current_node.right = MyTreeNode(new_data)
        else:
            linked_insert(current_node.right, new_data)
    else:
        if current_node.left is None:
            current_node.left = MyTreeNode(new_data)
        else:
            linked_insert(current_node.left, new_data)


def pre_order_print(current_node):
    if current_node is not None:
        print current_node.data_value,
        if current_node.left is not None:
            pre_order_print(current_node.left)
        if current_node.right is not None:
            pre_order_print(current_node.right)


def pre_order_search(current_node, key):
    if current_node is None:
        return False
    else:
        if current_node.data_value == key:
            return True
        if current_node.val > key:
            return pre_order_search(current_node.left, key)
        return pre_order_search(current_node.right, key)
