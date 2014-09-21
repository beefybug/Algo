import random
from sort import insertSort, quickSort, mergeSort

data = [i for i in range(200)]
baseData = [i for i in range(200)]


for i in range(10):
    random.shuffle(data)
    insertSort(data)
    print(data == baseData)

for i in range(10):
    random.shuffle(data)
    quickSort(data)
    print(data == baseData)

for i in range(10):
    random.shuffle(data)
    mergeSort(data)
    print(data == baseData)
