'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    z = 0  # last non-zero value found at
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[z] = arr[z], arr[i]
            z = i

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
