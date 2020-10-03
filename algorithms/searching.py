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


def binary_search(arr, item):
    pass


###

print(linear_search(one, 7))
