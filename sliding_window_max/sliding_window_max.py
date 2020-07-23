'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # k = window size
    # windows moves right 1 index at a time
    window_start = 0
    window_end = k
    arr = []
    while window_end <= len(nums):
        largest = nums[window_start]
        for n in range(window_start, window_end):
            if nums[n] > largest:
                largest = nums[n]
        arr.append(largest)
        window_start += 1
        window_end += 1
    return arr
             


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
