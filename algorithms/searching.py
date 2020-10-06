from sorting import merge_sort
import math

one = [1, 4, 6, 7, 1, 5, 3, 8, 5, 9, 2, 2]
two = [3, 1, 4, 1, 5, 9, 2, 6, 3, 5, 8, 5]
tee = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
fou = [4, 45, 39, 6, 48, 16, 37, 27, 28, 3, 47, 5, 20, 51, 49]


def linear_search(arr, item):
    # doesn't take account dupes
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1


def binary_search_recursive(arr, item, start, end):
    mid = (start + end) // 2
    if item == arr[mid]:
        return mid
    if item < arr[mid]:
        return binary_search_recursive(arr, item, start, mid - 1)
    if item > arr[mid]:
        return binary_search_recursive(arr, item, mid + 1, end)


def binary_search(arr, item):
    start = 0
    end = len(arr)

    while start <= end:
        mid = (start + end) // 2
        if item == arr[mid]:
            return mid
        if item < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def jump_search_linear(arr, item):
    # TC: O(sqrt(n)), where sqrt(n) is jump size
    # better over binary search in large n because no / operator
    # make faster with jumps having binary search
    size = len(arr)
    jump = int(math.sqrt(size))
    left = 0
    right = 0
    while left < size and arr[left] <= item:
        right = min(size - 1, left + jump)
        if arr[left] <= item <= arr[right]:
            break
        left += jump
    if left >= size or arr[left] > item:
        return -1
    right = min(size - 1, right)
    i = left
    while i <= right and arr[i] <= item:
        if arr[i] == item:
            return i
        i += 1
    return -1


def fibonacci_search(arr, item):
    pass


def exponential_search(arr, item):
    # TC: O(log i), where i is index of item
    # Worst: O(log n)
    # better for infinite arrays
    if arr[0] == item:
        return 0
    i = 1
    size = len(arr)
    while i < size and arr[i] <= item:
        i *= 2
    return binary_search(arr[:min(i, size)], item)


def interpolation_search(arr, item):
    pass


###

print("Sort")
merge_sort(tee)
print(tee)
# print(binary_search_recursive(tee, 36, 0, len(tee) - 1))
print(exponential_search(tee, 36))
