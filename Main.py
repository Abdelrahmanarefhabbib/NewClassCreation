from DataStructuresManager import DataStructuresManager


myManager = DataStructuresManager()
myManager.create_new_binary_tree()
myManager.binary_trees[0].insert(5)
myManager.binary_trees[0].insert(1)
myManager.binary_trees[0].insert(10)
myManager.binary_trees[0].insert(3)
myManager.binary_trees[0].insert(7)

myManager.print_all_binary_trees()
# print myManager.binary_trees[0].get_max()
myManager.binary_trees[0].delete(5)
myManager.print_all_binary_trees()

