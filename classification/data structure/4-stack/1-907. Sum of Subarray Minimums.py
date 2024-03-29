'''
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr.
Since the answer may be large, return the answer modulo 10**9 + 7.

Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
'''

def sumSubarrayMins_TLE(arr):
    ret = 0
    stack = []
    for i,n in enumerate(arr):
        while stack and arr[stack[-1]]>n:
            stack.pop()
        stack.append(i)

        prev = -1
        for cur in stack:
            ret += (cur-prev)*arr[cur]
            prev = cur
    return ret

def sumSubarrayMins(arr):
    stack = [[-1, 0]]
    cursum = 0
    for i, n in enumerate(arr):
        while len(stack) > 1 and arr[stack[-1][0]] > n:
            cursum += stack.pop()[1]

        stack.append([i, (i - stack[-1][0]) * n + stack[-1][1]])
    return (sum(list(zip(*stack))[1]) + cursum) % (10 ** 9 + 7)

arr = [3,1]
print(sumSubarrayMins(arr))