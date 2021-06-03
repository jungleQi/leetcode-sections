'''
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ
, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5]
because the first position they differ is at the final number, and 4 is less than 5.

Example 1:
Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
'''

def mostCompetitive(nums, k):
    stack = []
    N = len(nums)
    M = 0
    for i, num in enumerate(nums):
        while stack and stack[-1] > num and M + N - i > k:
            stack.pop()
            M -= 1
        stack.append(num)
        M += 1
    return stack[:k]

nums = [1,3,2,4]
k = 2
print(mostCompetitive(nums, k))