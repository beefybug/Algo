import random
import time
from sort import insertSort, quickSort, mergeSort

data = [i for i in range(200)]
baseData = [i for i in range(200)]

num = 1000

start = time.clock()
for i in range(num):
    random.shuffle(data)
    insertSort(data)
    if data != baseData:
        print("Insertion Sort issue")
print("Insertion sort takes on average {:.5f}".format((time.clock()-start)/num))


start = time.clock()
for i in range(num):
    random.shuffle(data)
    quickSort(data)
    if data != baseData:
        print("Quick Sort issue")
print("Quick sort takes on average {:5f}".format((time.clock()-start)/num))


start = time.clock()
for i in range(num):
    random.shuffle(data)
    mergeSort(data)
    if data != baseData:
        print("Merge Sort issue")
print("Merge sort takes on average {:5f}".format((time.clock()-start)/num))
