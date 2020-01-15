from DataStructuresManager import DataStructuresManager


myManager = DataStructuresManager()
myManager.create_new_heap()
myManager.heaps[0].push(1)
myManager.heaps[0].push(2)
myManager.heaps[0].push(3)
myManager.heaps[0].push(5)
myManager.heaps[0].push(7)

print myManager.print_all_heaps()
