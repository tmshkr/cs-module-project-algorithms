from functools import reduce
'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

"""
O(n) time, O(n) space

def single_number(arr):
    counter = {}
    for num in arr:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    for num in counter:
        if counter[num] == 1:
            return num
"""

"""
# O(n) time, O(1) space

Bitwise XOR will cancel out duplicates, leaving the single number
"""


def single_number(arr):
    return reduce(lambda a, b: a ^ b, arr)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
