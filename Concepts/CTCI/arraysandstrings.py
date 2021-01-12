"""
1.1 Is Unique
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""
string_1 = "abcd" # True
string_2 = "abca" # False
string_empty = "" # True
string_single = "a" # True


# Method 1: Use a hashtable
def string_is_unique(str) -> bool:
    """
    Uses a hashmap for storing unique values
    Returns false if already in the hashmap
    O(A) characters and O(1) search so O(N) time
    O(A) space
    :param str:
    :return bool:
    """
    char_count = {}
    for c in str:
        if c in char_count:
            return False
        char_count[c] = 1
        # print(char_count)
    return True

# print(string_is_unique(string_1))
# print(string_is_unique(string_2))
# print(string_is_unique(string_empty))
# print(string_is_unique(string_single))

# Method 2: Use a queue (list)
# Method 3: Use a set

# Method 4: Space O(1)
def string_is_unique_space(str) -> bool:
    """
    Uses brute force to check for each character
    Utilizes enumerate for indexing the str
    Returns false if ==
    No extra space used
    Is O(N^2) and O(1)
    """
    # count = 0
    for i,c in enumerate(str):
        for j,d in enumerate(str):
            if (i != j) and (str[i] == str[j]):
                return False
            # count += 1
    # print(count)
    return True

print(string_is_unique_space(string_1))
print(string_is_unique_space(string_2))
print(string_is_unique_space(string_empty))
print(string_is_unique_space(string_single))

"""
1.2 Check Permutation
Given two strings, decide if one is a permutation of the other
"""
print("Problem 1.2: ")
pstr_1 = "abcd"
pstr_2 = "adb"
pstr_3 = "bda"
pstr_4 = "a"
pstr_5 = ""

# Method 1: loop through each one once and hashmap
def is_permutation_map(curr, str):
    """
    Uses a hashmap to store values of each string
    If different sizes return false
    is O(N) time = len(curr) + len(str) + intersection(curr, str)
    O(curr + str - (curr and str) space
    :param curr:
    :param str:
    :return:
    """
    # make sure they are the same size
    if len(curr) != len(str):
        return False
    count = {}
    for i,c in enumerate(str):
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    for i,c in enumerate(curr):
        if c in count:
            count[c] -= 1
        else:
            count[c] = 1
    for k,v in count.items():
        if v != 0:
            return False
    return True

print("Should be False: ", is_permutation_map(pstr_1, pstr_2))
print("Should be True: ", is_permutation_map(pstr_2, pstr_3))
print("Should be True: ", is_permutation_map(pstr_3, pstr_2))
print("Should be False: ", is_permutation_map(pstr_4, pstr_5))


# Method 2: difference of sets
# if difference set == {} then return True O(N) time, O(N) spce
# Method 3: for space
# ???

"""
1.3 URLify

"""