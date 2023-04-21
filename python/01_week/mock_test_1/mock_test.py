def findMedian(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[len(sorted_arr) // 2]


print(findMedian([0, 1, 2, 4, 6, 5, 3]))
