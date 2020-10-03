import numpy as np
from heapq import heappop, heappush

one = [1, 4, 6, 7, 1, 5, 3, 8, 5, 9, 2, 2]
two = [3, 1, 4, 1, 5, 9, 2, 6, 3, 5, 8, 5]
tee = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
fou = [4, 45, 39, 6, 48, 16, 37, 27, 28, 3, 47, 5, 20, 51, 49]


def selection_sort_basic(li):
    for i in range(len(li)):
        left_i = i
        for j in range(i + 1, len(li)):
            if li[left_i] > li[j]:
                left_i = j
        li[i], li[left_i] = li[left_i], li[i]


def selection_sort(li):
    for i in range(len(li)):
        # argmin returns index of min ele in array in some axis
        left_i = i + np.argmin(li[i:])
        li[i], li[left_i] = li[left_i], li[i]


def bubble_sort(li):
    for i in range(len(li)):
        for j in range(len(li) - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


def insert_sort(li):
    for i in range(1, len(li)):
        hold = li[i]
        right = i - 1
        while right >= 0 and hold < li[right]:
            li[right + 1] = li[right]
            right -= 1
        li[right + 1] = hold


def merge_sort(li):
    if len(li) > 1:
        mid = len(li) // 2
        L = li[:mid]
        R = li[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Go through both copies until we run out of elements in one
        while i < len(L) and j < len(R):
            # If our left_copy has the smaller element, put it in the sorted
            # part and then move forward in left_copy (by increasing the pointer)
            if L[i] < R[j]:
                li[k] = L[i]
                i += 1
            # Opposite from above
            else:
                li[k] = R[j]
                j += 1
            # Regardless of where we got our element from
            # move forward in the sorted part
            k += 1

        # Checking if any element was left
        # We ran out of elements either in left_copy or right_copy
        # so we will go through the remaining elements and add them
        while i < len(L):
            li[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            li[k] = R[j]
            j += 1
            k += 1


def partition(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= pivot:
            high -= 1
        while low <= high and arr[low] <= pivot:
            low += 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]

    return high


def quick_sort_first(li, start, end):
    if start >= end:
        return

    p = partition(li, start, end)
    quick_sort_first(li, start, p - 1)
    quick_sort_first(li, p + 1, end)


def heap_sort(array):
    # use heap sort when memory > performance
    # merge sort when performance > memory
    heap = []
    for element in array:
        heappush(heap, element)

    # gives copy of sorted array
    ordered = []

    # While we have elements left in the heap
    while heap:
        ordered.append(heappop(heap))

    return ordered



###

print('Sort: \n')
# quick_sort_first(tee, 0, len(fou) - 1)
# print(fou)
print(heap_sort(tee))
