from MyTreeNode import MyTreeNode


class MyAVLTree:
    def __init__(self):
        self.root = None

    def print_tree(self):
        pre_order_print(self.root)

    def insert(self, new_data):
        self.root = self.insert_and_fix_tree(self.root, new_data)

    def insert_and_fix_tree(self, node, new_data):
        if node is None:
            return MyTreeNode(new_data)
        elif new_data < node.data_value:
            node.left = self.insert_and_fix_tree(node.left, new_data)
        else:
            node.right = self.insert_and_fix_tree(node.right, new_data)

        node.height = 1 + max(get_height(node.right), get_height(node.left))
        balance_factor = get_balance_factor(node)

        # Left Left
        if balance_factor > 1 and new_data < node.left.data_value:
            return right_rotate(node)

        # Left Right
        if balance_factor > 1 and new_data > node.left.data_value:
            node.left = left_rotate(node.left)
            return right_rotate(node)

        # Right Right
        if balance_factor < -1 and new_data > node.right.data_value:
            return left_rotate(node)

        # Right Left
        if balance_factor < -1 and new_data < node.right.data_value:
            node.right = right_rotate(node.right)
            return left_rotate(node)

        return node

    def delete(self, key):
        self.root = self.delete_and_fix_tree(self.root, key)

    def delete_and_fix_tree(self, node, key):
        if not node:
            return node
        elif key < node.data_value:
            node.left = self.delete_and_fix_tree(node.left, key)
        elif key > node.data_value:
            node.right = self.delete_and_fix_tree(node.right, key)

        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.data_value = get_min_in_sub_tree(node.right)
            node.right = self.delete_and_fix_tree(node.right, node.data_value)

        if node is None:
            return node

        node.height = 1 + max(get_height(node.left), get_height(node.right))

        # Step 3 - Get the balance factor
        balance = get_balance_factor(node)

        # Left Left
        if balance > 1 and get_balance_factor(node.left) >= 0:
            return right_rotate(node)

        #  Left Right
        if balance > 1 and get_balance_factor(node.left) < 0:
            node.left = left_rotate(node.left)
            return right_rotate(node)

        # Right Right
        if balance < -1 and get_balance_factor(node.right) <= 0:
            return left_rotate(node)

        # Right Left
        if balance < -1 and get_balance_factor(node.right) > 0:
            node.right = right_rotate(node.right)
            return left_rotate(node)

        return node

    def search(self, key):
        return pre_order_search(self.root, key)

    def get_min(self, node=None):
        if node is None:
            node = self.root
        return get_min_in_sub_tree(node)

    def get_max(self):
        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.data_value


def get_height(node):
    if node is None:
        return 0
    return node.height


def left_rotate(current_node):
    right_child = current_node.right
    left_child_of_right_child = right_child.left
    right_child.left = current_node
    current_node.right = left_child_of_right_child

    current_node.height = 1 + max(get_height(current_node.left), get_height(current_node.right))
    right_child.height = 1 + max(get_height(right_child.left), get_height(right_child.right))
    return right_child


def right_rotate(current_node):
    left_child = current_node.left
    right_child_of_left_child = left_child.right
    left_child.right = current_node
    current_node.left = right_child_of_left_child

    current_node.height = 1 + max(get_height(current_node.left), get_height(current_node.right))
    left_child.height = 1 + max(get_height(left_child.left), get_height(left_child.right))
    return left_child


def get_balance_factor(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)


def pre_order_print(current_node):
    if current_node is not None:
        print current_node.data_value,
        if current_node.left is not None:
            pre_order_print(current_node.left)
        if current_node.right is not None:
            pre_order_print(current_node.right)


def get_min_in_sub_tree(current_node):
    while current_node.left is not None:
        current_node = current_node.left
    return current_node.data_value


def pre_order_search(current_node, key):
    if current_node is None:
        return False
    else:
        if current_node.data_value == key:
            return True
        if current_node.data_value > key:
            return pre_order_search(current_node.left, key)
        return pre_order_search(current_node.right, key)
