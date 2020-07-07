'''
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s.

Example 1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
'''

def longestOnes(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    start = end = oneCnt = 0
    N = len(A)

    maxLen = 0
    while end < N:
        oneCnt += A[end]
        end += 1

        if end - start - oneCnt <= K:
            maxLen = max(maxLen, end - start)
        else:
            oneCnt -= A[start]
            start += 1

    return maxLen

# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]