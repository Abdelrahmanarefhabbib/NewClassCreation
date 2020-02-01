from DataStructuresManager import DataStructuresManager


def linked_list_example(my_manager):
    my_manager.create_new_linked_list()
    my_manager.linked_lists[0].add_node("a")
    my_manager.linked_lists[0].add_node("b")
    my_manager.linked_lists[0].add_node("c")
    my_manager.linked_lists[0].add_node("d")
    my_manager.linked_lists[0].add_node("e")

    print "The linked list: ",
    my_manager.print_all_linked_lists()
    my_manager.linked_lists[0].remove_node_by_key("d")
    print "The list after d was deleted: ",
    my_manager.print_all_linked_lists()
    print


def stack_example(my_manager):
    my_manager.create_new_stack()
    my_manager.stacks[0].push(2)
    my_manager.stacks[0].push(4)
    my_manager.stacks[0].push(1)
    my_manager.stacks[0].push(10)

    print "Push order to stack 2, 4, 1, 10"
    print "Stack pop operation return: ", my_manager.stacks[0].pop()
    print "Stack pop operation return: ", my_manager.stacks[0].pop()
    print "Stack pop operation return: ", my_manager.stacks[0].pop()
    print "Stack pop operation return: ", my_manager.stacks[0].pop()
    print


def queue_example(my_manager):
    my_manager.create_new_queue()
    my_manager.queues[0].enqueue("a")
    my_manager.queues[0].enqueue("b")
    my_manager.queues[0].enqueue("c")
    my_manager.queues[0].enqueue("d")

    print "Enqueue order to queue a, b, c, d"
    print "Front element is:", my_manager.queues[0].front()
    print "Rear element is: ", my_manager.queues[0].rear()
    print "Dequeue operation return: ", my_manager.queues[0].dequeue()
    print "Dequeue operation return: ", my_manager.queues[0].dequeue()
    print "Dequeue operation return: ", my_manager.queues[0].dequeue()
    print "Dequeue operation return: ", my_manager.queues[0].dequeue()
    print


def heap_example(my_manager):
    my_manager.create_new_heap()
    my_manager.heaps[0].push(1)
    my_manager.heaps[0].push(3)
    my_manager.heaps[0].push(5)
    my_manager.heaps[0].push(2)
    my_manager.heaps[0].push(4)
    my_manager.heaps[0].push(8)

    print "Push order to heap: 1, 3, 5, 2, 4, 8"
    print "The heap keys: ",
    myManager.print_all_heaps()
    my_manager.heaps[0].pop(1)
    print "The heap after 2 (index 1) is deleted: ",
    myManager.print_all_heaps()
    print


def binary_search_tree_example(my_manager):
    my_manager.create_new_binary_tree()
    my_manager.binary_trees[0].insert(5)
    my_manager.binary_trees[0].insert(3)
    my_manager.binary_trees[0].insert(7)
    my_manager.binary_trees[0].insert(2)
    my_manager.binary_trees[0].insert(4)
    my_manager.binary_trees[0].insert(1)
    my_manager.binary_trees[0].insert(0)

    print "Push order to binary search tree: 5, 3, 7, 2, 4, 1, 0"
    print "The binary search tree keys: ",
    myManager.print_all_binary_trees()
    my_manager.binary_trees[0].delete(3)
    print "The binary search tree after 3 is deleted: ",
    myManager.print_all_binary_trees()
    print


def AVL_tree_example(my_manager):
    my_manager.create_new_avl_tree()
    my_manager.avl_trees[0].insert(5)
    my_manager.avl_trees[0].insert(3)
    my_manager.avl_trees[0].insert(7)
    my_manager.avl_trees[0].insert(2)
    my_manager.avl_trees[0].insert(4)
    my_manager.avl_trees[0].insert(1)
    my_manager.avl_trees[0].insert(0)

    print "Push order to AVL tree: 5, 3, 7, 2, 4, 1, 0"
    print "The AVL tree keys: ",
    myManager.print_all_avl_trees()
    my_manager.avl_trees[0].delete(3)
    print "The AVL tree after 3 is deleted: ",
    myManager.print_all_avl_trees()
    print


def two_three_tree_example(my_manager):
    my_manager.create_new_two_three_tree()
    my_manager.two_three_trees[0].insert(5)
    my_manager.two_three_trees[0].insert(1)
    my_manager.two_three_trees[0].insert(10)
    my_manager.two_three_trees[0].insert(3)
    my_manager.two_three_trees[0].insert(2)
    my_manager.two_three_trees[0].insert(4)

    print "search on 20: ", my_manager.two_three_trees[0].search(20)
    print "search on 2: ", my_manager.two_three_trees[0].search(2)
    my_manager.print_all_two_three_trees()
    print


myManager = DataStructuresManager()
linked_list_example(myManager)
stack_example(myManager)
queue_example(myManager)
heap_example(myManager)
binary_search_tree_example(myManager)
AVL_tree_example(myManager)
two_three_tree_example(myManager)


