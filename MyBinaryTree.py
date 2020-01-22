from MyTreeNode import MyTreeNode


class MyBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, new_data):
        if self.root is None:
            self.root = MyTreeNode(new_data)

        else:
            current_node = self.root
            found_empty_spot = False
            while not found_empty_spot:
                if current_node.data_value < new_data:
                    if current_node.right is None:
                        current_node.right = MyTreeNode(new_data)
                        found_empty_spot = True
                    else:
                        current_node = current_node.right
                else:
                    if current_node.left is None:
                        current_node.left = MyTreeNode(new_data)
                        found_empty_spot = True
                    else:
                        current_node = current_node.left

    def print_tree(self):
        pre_order_print(self.root)

    def search(self, key):
        return pre_order_search(self.root, key)

    def delete(self, key):
        if not self.search(key):
            return
        else:
            recursive_delete(self.root, key)

    def get_min(self, node=None):
        if node is None:
            node = self.root
        return get_min_in_sub_tree(node)

    def get_max(self):
        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.data_value


def get_min_in_sub_tree(current_node):
    while current_node.left is not None:
        current_node = current_node.left
    return current_node.data_value


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
        if current_node.data_value > key:
            return pre_order_search(current_node.left, key)
        return pre_order_search(current_node.right, key)


def recursive_delete(current_node, key):
    if current_node is None:
        return current_node

    if key < current_node.data_value:
        current_node.left = recursive_delete(current_node.left, key)

    elif key > current_node.data_value:
        current_node.right = recursive_delete(current_node.right, key)

    else:
        if current_node.left is None:
            return current_node.right

        elif current_node.right is None:
            return current_node.left

        current_node.data_value = get_min_in_sub_tree(current_node.right)
        current_node.right = recursive_delete(current_node.right, current_node.data_value)

    return current_node
