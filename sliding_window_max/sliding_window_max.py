'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque


def sliding_window_max(nums, k):
    result = []
    q = deque()

    for i in range(len(nums)):
        # pop off the last index in the queue
        # as long as the number at the current
        # index is greater than the number
        # at the last index in the queue,
        # so that it will only store indicies of max values
        while q and nums[i] > nums[q[-1]]:
            q.pop()
        # append the current index in order to
        # deal with it on the next iteration
        q.append(i)
        # dequeue if the first index is outside of the window
        if i - q[0] >= k:
            q.popleft()
        # if we've filled up the sliding window,
        # append the number at the first index in the queue to the result,
        # which will be the maximum value in the window at the current position
        if i >= k - 1:
            result.append(nums[q[0]])

    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
