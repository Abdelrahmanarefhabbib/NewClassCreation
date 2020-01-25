from DataStructuresManager import DataStructuresManager


myManager = DataStructuresManager()
myManager.create_new_two_three_tree()
myManager.two_three_trees[0].insert(5)
myManager.two_three_trees[0].insert(1)
myManager.two_three_trees[0].insert(10)
myManager.two_three_trees[0].insert(3)
myManager.two_three_trees[0].insert(2)
myManager.two_three_trees[0].insert(4)

myManager.print_all_two_three_trees()
