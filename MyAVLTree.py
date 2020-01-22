from MyTreeNode import MyTreeNode


class MyAVLTree:
    def __init__(self):
        self.root = None

    def insert(self, new_data):
        if self.root is None:
            self.root = MyTreeNode(new_data)

        else:
            binary_tree_insert(self.root)
            return


def binary_tree_insert(node, new_data):
    current_node = node
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

    current_node.height = 1 + max(get_height(current_node.right), get_height(current_node.left))
    balance_factor = get_balance_factor(current_node)

    #   TODO implement the cases
    # Case 1 - Left Left
    if balance_factor > 1 and key < current_node.left.val:
        return self.rightRotate(current_node)

        # Case 2 - Right Right
    if balance_factor < -1 and key > current_node.right.val:
        return self.leftRotate(current_node)

        # Case 3 - Left Right
    if balance_factor > 1 and key > current_node.left.val:
        root.left = self.leftRotate(current_node.left)
        return self.rightRotate(current_node)

        # Case 4 - Right Left
    if balance_factor < -1 and key < current_node.right.val:
        root.right = self.rightRotate(current_node.right)
        return self.leftRotate(current_node)

def get_height(node):
    if node is None:
        return 0
    return node.height


def get_balance_factor(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)
