import random
import time
import copy
from sort import insertSort, quickSort, mergeSort

data = [i for i in range(200)]
baseData = [i for i in range(200)]
res = []

num = 1000

for i in range(num):
    random.shuffle(data)
    res.append(copy.copy(data))


start = time.clock()
for i in range(num):
    temp = copy.copy(res[i])
    insertSort(temp)
    if temp != baseData:
        print("Insertion Sort issue")
print("Insertion sort takes on average {:.5f}".format((time.clock()-start)/num))


start = time.clock()
for i in range(num):
    temp = copy.copy(res[i])
    quickSort(temp)
    if temp != baseData:
        print("Quick Sort issue")
print("Quick sort takes on average {:5f}".format((time.clock()-start)/num))


start = time.clock()
for i in range(num):
    temp = copy.copy(res[i])
    mergeSort(temp)
    if temp != baseData:
        print("Merge Sort issue")
print("Merge sort takes on average {:5f}".format((time.clock()-start)/num))
