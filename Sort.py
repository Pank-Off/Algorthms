import time
import random

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        less = []
        greater = []
        pivot = arr[0]
        for i in range(len(arr)):
            if arr[i] < pivot:
                less.append(arr[i])
            if arr[i] > pivot:
                greater.append(arr[i])
        return quickSort(less) + [pivot] + quickSort(greater)


def putSort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j = j - 1
    return arr


def choiseSort(arr):
    for i in range(0, len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
    return arr


array = [random.randint(0, 10000000) for i in range(0, 10000)]
start_time = time.time()
print(quickSort(array))
print((time.time() - start_time))

array = [random.randint(0, 10000000) for i in range(0, 10000)]
start_time = time.time()
print(putSort(array))
print((time.time() - start_time))


array = [random.randint(0, 10000000) for i in range(0, 10000)]
start_time = time.time()
print(choiseSort(array))
print((time.time() - start_time))