#coding=utf-8

'''
Given an array of integers, return the maximum sum for a non-empty subarray
(contiguous elements) with at most one element deletion.

In other words, you want to choose a subarray and optionally delete one element from it so that
there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

Example 1:
Input: arr = [1,-2,0,3]
Output: 4
Explanation:
Because we can choose [1, -2, 0, 3] and drop -2,
thus the subarray [1, 0, 3] becomes the maximum value.
'''

#define state:
#   delete[i] 到i为止，删除一个元素后的子数组的最大和(可能包含或者不包含i)
#   keep[i] 到i为止，没删除元素的子数组的最大和(包含i)
def maximumSum(arr):
    N = len(arr)
    arr = [0] + arr

    delete, keep = [-float("inf")] + [0] * N, [-float("inf")] + [0] * N
    for i in range(1, N + 1):
        delete[i] = max(delete[i - 1] + arr[i], keep[i - 1])
        keep[i] = max(0, keep[i - 1]) + arr[i]

    return max(max(delete), max(keep))

def maximumSum_concise(arr):
    ret = delete = keep = arr[0]
    for num in arr[1:]:
        delete = max(delete + num, keep)
        keep = max(0, keep) + num
        ret = max(delete, keep, ret)
    return ret

arr = [8,-1,6,-7,-4,5,-4,7,-6]
print(maximumSum(arr))

#case 1, we don't delete anything, which can be solved by max subarray problem
#case 2, we only delete one element.
#dp1 to store the max subarray ended with positive i. dp2 to store max subarray started at positive i.