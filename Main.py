from DataStructuresManager import DataStructuresManager


myManager = DataStructuresManager()
myManager.create_new_avl_tree()
myManager.avl_trees[0].insert(5)
myManager.avl_trees[0].insert(1)
myManager.avl_trees[0].insert(10)
myManager.avl_trees[0].insert(3)
myManager.avl_trees[0].insert(2)
myManager.avl_trees[0].insert(4)


myManager.print_all_avl_trees()

