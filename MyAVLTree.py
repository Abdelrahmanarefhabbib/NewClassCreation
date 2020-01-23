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
            return rightRotate(node)

        # Left Right
        if balance_factor > 1 and new_data > node.left.data_value:
            node.left = leftRotate(node.left)
            return rightRotate(node)

        # Right Right
        if balance_factor < -1 and new_data > node.right.data_value:
            return leftRotate(node)

        # Right Left
        if balance_factor < -1 and new_data < node.right.data_value:
            node.right = rightRotate(node.right)
            return leftRotate(node)

        return node


def get_height(node):
    if node is None:
        return 0
    return node.height


def leftRotate (current_node):
    right_child = current_node.right
    left_child_of_right_child = right_child.left
    right_child.left = current_node
    current_node.right = left_child_of_right_child

    current_node.height = 1 + max(get_height(current_node.left), get_height(current_node.right))
    right_child.height = 1 + max(get_height(right_child.left), get_height(right_child.right))
    return right_child


def rightRotate(current_node):
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