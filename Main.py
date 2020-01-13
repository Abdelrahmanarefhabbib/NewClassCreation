from DataStructuresManager import DataStructuresManager


myManager = DataStructuresManager()
myManager.create_new_heap(10)
myManager.heaps[0].push(1)
myManager.heaps[0].push(2)
myManager.heaps[0].push(3)
myManager.heaps[0].push(5)
myManager.heaps[0].push(7)
myManager.heaps[0].push(4)
myManager.heaps[0].print_heap()
print
myManager.heaps[0].pop(0)
myManager.heaps[0].print_heap()
