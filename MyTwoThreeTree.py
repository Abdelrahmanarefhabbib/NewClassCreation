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
                        if new_data < current_node.right.data_values[0]:
                            current_node.right.data_values.insert(0, new_data)
                        else:
                            current_node.right.data_values.insert(1, new_data)
                    # Case 2
                        if len(current_node.data_values) == 1:
                            current_node.data_values.append(current_node.right.data_values.pop(1))
                    # Case 3
                        elif len(current_node.data_values) == 2:
                            if new_data > current_node.data_values[1]:
                                current_node.data_values.insert(2, new_data)
                            if new_data < current_node.data_values[0]:
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

                if new_data < min(current_node.data_values):
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
                        if new_data < current_node.left.data_values[0]:
                            current_node.left.data_values.insert(0, new_data)
                        else:
                            current_node.left.data_values.insert(1, new_data)
                    # Case 2
                        if len(current_node.data_values) == 1:
                            current_node.data_values.append(current_node.left.data_values.pop(1))
                    # Case 3
                        elif len(current_node.data_values) == 2:
                            if new_data > current_node.data_values[1]:
                                current_node.data_values.insert(2, new_data)
                            if new_data < current_node.data_values[0]:
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
#TODO set this right with middle
                else:
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
                        if new_data < current_node.left.data_values[0]:
                            current_node.left.data_values.insert(0, new_data)
                        else:
                            current_node.left.data_values.insert(1, new_data)
                    # Case 2
                        if len(current_node.data_values) == 1:
                            current_node.data_values.append(current_node.left.data_values.pop(1))
                    # Case 3
                        elif len(current_node.data_values) == 2:
                            if new_data > current_node.data_values[1]:
                                current_node.data_values.insert(2, new_data)
                            if new_data < current_node.data_values[0]:
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
                    pass