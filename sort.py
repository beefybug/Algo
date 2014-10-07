__all__ = ['insertSort', 'quickSort', 'mergeSort']
# when using from sort import *, only those in __all__ can be seen
import random


def insertSort(data):
    for i in range(1, len(data)):
        key = data[i]  # Current value that I am sorting
        # print("Key is {}".format(key))
        j = i-1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]  # Swap when the value is bigger than key
            j -= 1
        data[j+1] = key


def quickSort(data):
    """Wrapper for the quickSorter function which implements quick sort"""
    quickSorter(data, 0, len(data) - 1)


def quickSorter(data, i, j):
    if i < j:
        # All other cases are trivial and does not require sorting
        split = partition(data, i, j)
        quickSorter(data, i, split-1)
        quickSorter(data, split+1, j)


def partition(data, i, j):
    """Returns the position of the key and seperate the rest"""
    key = data[j]
    pivot = i-1
    for k in range(i, j):
        if data[k] <= key:
            pivot += 1
            data[k], data[pivot] = data[pivot], data[k]
    pivot += 1
    data[j], data[pivot] = data[pivot], data[j]
    return pivot


def rquickSort(data):
    """Wrapper for the rquickSorter function which
    implements random quick sort"""
    rquickSorter(data, 0, len(data)-1)


def rquickSorter(data, i, j):
    if i < j:
        split = rpartition(data, i, j)
        rquickSorter(data, i, split-1)
        rquickSorter(data, split+1, j)


def rpartition(data, i, j):
    # calling random,randint seems like the bottleneck
    k = random.randint(i, j)
    data[j], data[k] = data[k], data[j]
    return partition(data, i, j)


def mergeSort(data):
    """Wraper for mergeSorter"""
    mergeSorter(data, 0, len(data)-1)


def merge(L, R):
    """Combines back into data
    Assumes that the inputs are sorted in ascending order"""
    data = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            data.append(L[i])
            i += 1
        else:
            data.append(R[j])
            j += 1
    if i == len(L):
        # Means that L copied finish
        data.extend(R[j:])
    else:
        data.extend(L[i:])
    return data


def mergeSorter(data, i, j):
    """ Sorts between the index i and j"""
    if i < j:
        # Get the middle and split the
        middle = i + ((j-i) // 2)
        mergeSorter(data, i, middle)
        mergeSorter(data, middle+1, j)
        data[i:j+1] = merge(data[i:(middle+1)], data[(middle+1):(j+1)])


def main():
    a = [5, 12, 4, 1, 2, 12]
    quickSort(a)
    print(a)
    print("hello")

if __name__ == "__main__":
    main()
