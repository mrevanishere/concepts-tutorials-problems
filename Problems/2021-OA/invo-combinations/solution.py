import itertools

# Definition of the num pad
# Like a phone num pad
digit_to_letter: dict = {0: [""], 1: [""], 2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"],
                         5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 8: ["t", "u", "v"],
                         9: ["w", "x", "y", "z"]}


def findCombinations(digits: str, search: str):
    """
    Given a string of digits, and a string of a word,
    return a list of all combinations of letters that 
    contains the search word from the digits.

    1. First find search string and remove it
    2. Generate combinations: for each digit in digits get each letter for each digit and
    then for each combo in the combo list append the next letter
    3. add back search string
    """
    # for i in range(0, len(digits)):
    #     for c in digit_to_letter[digits[i]]:
    #         pass

    # 1st pass find str in digits
    in_string = []
    i = 0
    pos = 0
    for digit in digits:
        if search[i] in digit_to_letter[int(digit)]:
            i += 1
            # print(i)
            if i == len(search):
                # print(digits[0:pos-i+1])
                # print(digits[pos+1:])
                left = digits[0:pos-i+1]
                right = digits[pos+1:]
                digits = left + right
                break
            in_string.append(True)
        else:
            i = 0
            in_string.append(False)
        pos += 1
    print(digits)

    # 2nd pass: generate combinations
    all_combo = [''] if digits else []
    for digit in digits:
        curr_combo = []
        # print(digit)
        for letter in digit_to_letter[int(digit)]:
            for combination in all_combo:
                curr_combo.append(combination + letter)
        all_combo = curr_combo

    # 3rd pass: add back search
    for j in range(0, len(all_combo)):
        all_combo[j] = all_combo[j][0:pos-i+1] + search + all_combo[j][pos-i+1:]
    return all_combo


if __name__ == "__main__":
    # print(digit_to_letter[5])
    # for c in digit_to_letter[5]:
    # print(c)
    print(findCombinations("52283", "cat"))
    print(findCombinations("542283", "4cat"))
