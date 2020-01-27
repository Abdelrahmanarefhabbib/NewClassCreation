from MyTwoThreeNode import MyTwoThreeNode


class MyTwoThreeTree:
    def __init__(self):
        self.root = None

    def insert(self, new_data):
        if self.root is None:
            self.root = MyTwoThreeNode(new_data)

        else:
            current_node = self.root
            found_empty_spot = False
            while not found_empty_spot:
                if new_data > max(current_node.data_values):
                    if current_node.right is None:
                        current_node.right = MyTwoThreeNode(new_data)
                        found_empty_spot = True
                    # Case 1
                    elif len(current_node.right.data_values) == 1:
                        current_node.right.data_values.append(new_data)
                        found_empty_spot = True
                    # Case 2,3
                    elif len(current_node.right.data_values) == 2:
                        if new_data > current_node.right.data_values[1]:
                            current_node.right.data_values.insert(2, new_data)
                        elif new_data < current_node.right.data_values[0]:
                            current_node.right.data_values.insert(0, new_data)
                        else:
                            current_node.right.data_values.insert(1, new_data)
                    # Case 2
                        if len(current_node.data_values) == 1:
                            current_node.data_values.append(current_node.right.data_values.pop(1))
                            current_node.middle.data_values.append(current_node.right.data_values.pop(0))
                    # Case 3
                        elif len(current_node.data_values) == 2:
                            if new_data > current_node.data_values[1]:
                                current_node.data_values.insert(2, new_data)
                            elif new_data < current_node.data_values[0]:
                                current_node.data_values.insert(0, new_data)
                            else:
                                current_node.data_values.insert(1, new_data)

                            new_max_node = MyTwoThreeNode(current_node.data_values.pop())
                            new_min_node = MyTwoThreeNode(current_node.data_values.pop(0))
                            new_max_node.right = current_node.right
                            new_max_node.left = current_node.right.data_values.pop(0)
                            new_min_node.left = current_node.left
                            new_min_node.right = current_node.middle

                            current_node.right = new_max_node
                            current_node.left = new_min_node
                            current_node.middle = None
                        found_empty_spot = True

                    else:
                        current_node = current_node.right

                elif new_data < min(current_node.data_values):
                    if current_node.left is None:
                        current_node.left = MyTwoThreeNode(new_data)
                        found_empty_spot = True
                    # Case 1
                    elif len(current_node.left.data_values) == 1:
                        current_node.left.data_values.append(new_data)
                        found_empty_spot = True
                    # Case 2,3
                    elif len(current_node.left.data_values) == 2:
                        if new_data > current_node.left.data_values[1]:
                            current_node.left.data_values.insert(2, new_data)
                        elif new_data < current_node.left.data_values[0]:
                            current_node.left.data_values.insert(0, new_data)
                        else:
                            current_node.left.data_values.insert(1, new_data)
                    # Case 2
                        if len(current_node.data_values) == 1:
                            current_node.data_values.append(current_node.left.data_values.pop(1))
                            current_node.middle = MyTwoThreeNode(current_node.left.data_values.pop(1))
                    # Case 3
                        elif len(current_node.data_values) == 2:
                            if new_data > current_node.data_values[1]:
                                current_node.data_values.insert(2, new_data)
                            elif new_data < current_node.data_values[0]:
                                current_node.data_values.insert(0, new_data)
                            else:
                                current_node.data_values.insert(1, new_data)

                            new_max_node = MyTwoThreeNode(current_node.data_values.pop())
                            new_min_node = MyTwoThreeNode(current_node.data_values.pop(0))
                            new_max_node.right = current_node.right
                            new_max_node.left = current_node.middle
                            new_min_node.left = current_node.left
                            new_min_node.right = current_node.left.data_values.pop()

                            current_node.right = new_max_node
                            current_node.left = new_min_node
                            current_node.middle = None
                        found_empty_spot = True

                else:
                    if current_node.middle is None:
                        current_node.middle = MyTwoThreeNode(new_data)
                        found_empty_spot = True
                    # Case 1
                    elif len(current_node.middle.data_values) == 1:
                        current_node.middle.data_values.append(new_data)
                        found_empty_spot = True
                    # Case 3
                    elif len(current_node.middle.data_values) == 2:
                        if new_data > current_node.middle.data_values[1]:
                            current_node.middle.data_values.insert(2, new_data)
                        elif new_data < current_node.middle.data_values[0]:
                            current_node.middle.data_values.insert(0, new_data)
                        else:
                            current_node.middle.data_values.insert(1, new_data)

                        if new_data > current_node.data_values[1]:
                            current_node.data_values.insert(2, new_data)
                        elif new_data < current_node.data_values[0]:
                            current_node.data_values.insert(0, new_data)
                        else:
                            current_node.data_values.insert(1, new_data)

                        new_max_node = MyTwoThreeNode(current_node.data_values.pop())
                        new_min_node = MyTwoThreeNode(current_node.data_values.pop(0))
                        new_max_node.right = current_node.right
                        new_max_node.left = current_node.middle.data_values.pop()
                        new_min_node.left = current_node.middle.data_values.pop()
                        new_min_node.right = current_node.left.data_values.pop()
                        current_node.right = new_max_node
                        current_node.left = new_min_node
                        current_node.middle = None

                        found_empty_spot = True

    def print_tree(self):
        pre_order_print(self.root)

    def delete(self, key):
        recursive_delete(self.root, key)

    def search(self, key):
        return pre_order_search(self.root, key)


def pre_order_print(current_node):
    if current_node is not None:
        print current_node.data_values,
        if current_node.left is not None:
            pre_order_print(current_node.left)
        if current_node.middle is not None:
            pre_order_print(current_node.middle)
        if current_node.right is not None:
            pre_order_print(current_node.right)


def recursive_delete(current_node, key):
    if current_node is None:
        return current_node

    if key < min(current_node.data_values):
        current_node.left = recursive_delete(current_node.left, key)
    elif key > max(current_node.data_values):
        current_node.right = recursive_delete(current_node.right, key)
    else:
        current_node.middle = recursive_delete(current_node.middle, key)

    if key in current_node.data_values:
        if len(current_node.data_values) == 1:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            current_node.data_values = get_min_in_sub_tree(current_node.right)
            current_node.right = recursive_delete(current_node.right, current_node.data_values[0])

        if len(current_node.data_values) == 2:
            if current_node.data_values[0] == key:
                key_index = 0
            else:
                key_index = 1

            if current_node.middle is None:
                current_node.data_values.pop(key_index)
            else:
                current_node.data_values[key_index] = current_node.middle.data_values.pop(0)
                if len(current_node.middle.data_values) == 0:
                    current_node.middle = None

    return current_node


def get_min_in_sub_tree(current_node):
    while current_node.left is not None:
        current_node = current_node.left
    return current_node.data_value


def pre_order_search(current_node, key):
    if current_node is None:
        return False
    else:
        if key in current_node.data_values:
            return True
        elif min(current_node.data_values) > key:
            return pre_order_search(current_node.left, key)
        elif max(current_node.data_values) < key:
            return pre_order_search(current_node.right, key)
        else:
            return pre_order_search(current_node.middle, key)
