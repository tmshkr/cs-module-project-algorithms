'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    z = 0  # will be the index of the last zero found
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[z], arr[i] = arr[i], arr[z]
            z += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [4, 0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
