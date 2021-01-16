# CTCI 17.5 Letters and Numbers
# see 525. Contiguous Array
"""
Given an array filled with letters and numbers find the longest subarray with
an equal number of letters and numbers

Ideas after reading 525:
convert arr to binary array (0 for num, 1 for letter)
and then brute force for O(n^2)
-> after looking at GFG this is how they do it.

"""

anstr = "d2hdj8zo9toxy002e401"  # 9 num, 11 letters
ans_1 = "9toxy002"
arr1: list = list(anstr)
anstr2 = "opo00o0o"  # 3 num, 5 letters
ans_2 = "po00o0"  # or "o00o0o"
arr2: list = list(anstr2)


def equal_letters_numbers(arr: list) -> list:
    i: int = 0
    j: int = len(arr)
    max: list = []
    while i < j:
        n: int = 0
        l: int = 0
        for k in range(i, j):  # there must be a more pythonic way: enum??
            if arr[k].isdigit():
                n += 1
            if arr[k].isalpha():
                l += 1

        if l == n:
            print(l, n)
            print(i, j)
            return arr[i:j]
        # idk how to increase/decrease
        j -= 1
        i += 1
    print(i, j)
    return [0]


def equal_letters_numbers_naive(arr: list) -> list:
    """
    Time: O(n^3)
    Mem: O(n)
    """

    print(len(arr))
    c = 0
    max: list = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            numbers: int = 0
            letters: int = 0
            c += 1
            for k in range(i, j):
                if arr[k].isdigit():
                    numbers += 1
                if arr[k].isalpha():
                    letters += 1
            print(c, numbers, letters, arr[i:j])
            if letters == numbers and len(arr[i:j]) > len(max):
                print("max reached")
                max = arr[i:j]
    return max


ans1 = equal_letters_numbers_naive(arr1)
print(len(ans1))
print(ans1)
# ans2 = equal_letters_numbers_naive(arr2)
# print(len(ans2))
# print(ans2)
