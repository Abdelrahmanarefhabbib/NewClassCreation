from MyTreeNode import MyTreeNode


class MyAVLTree:
    def __init__(self):
        self.root = None

    def insert(self, new_data):
        if self.root is None:
            self.root = MyTreeNode(new_data)

        else:
            parent_of_inserted_node = binary_tree_insert(self.root)
            parent_of_inserted_node.height = 1 + max(get_height(parent_of_inserted_node.right), get_height(parent_of_inserted_node.left))
            balance_factor = get_balance_factor(parent_of_inserted_node)

            # Case 1 - Left Left
            if balance_factor > 1 and new_data < parent_of_inserted_node.left.data_value:
                return self.rightRotate(parent_of_inserted_node)

                # Case 2 - Right Right
            if balance_factor < -1 and new_data > parent_of_inserted_node.right.data_value:
                return self.leftRotate(parent_of_inserted_node)

                # Case 3 - Left Right
            if balance_factor > 1 and new_data > parent_of_inserted_node.left.data_value:
                parent_of_inserted_node.left = self.leftRotate(parent_of_inserted_node.left)
                return self.rightRotate(parent_of_inserted_node)

                # Case 4 - Right Left
            if balance_factor < -1 and new_data < parent_of_inserted_node.right.data_value:
                parent_of_inserted_node.right = self.rightRotate(parent_of_inserted_node.right)
                return self.leftRotate(parent_of_inserted_node)

            return

    def leftRotate(self, z):
        new_root = z.right
        T2 = new_root.left
        # Perform rotation
        new_root.left = z
        z.right = T2
        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        # Return the new root
        return new_root

    def rightRotate(self, z):
        new_root = z.left
        T3 = new_root.right
        # Perform rotation
        new_root.right = z
        z.left = T3
        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        # Return the new root
        return new_root


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
    return current_node


def get_height(node):
    if node is None:
        return 0
    return node.height


def get_balance_factor(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)
