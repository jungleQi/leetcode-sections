import collections
def longestSubsequence(arr, difference):
    dp = collections.defaultdict(lambda :0)
    maxLen = 1
    for i in arr:
        dp[i] = dp[i-difference]+1
        maxLen = max(maxLen, dp[i])

    return maxLen

arr = [1]
#arr = [1,5,7,8,5]
difference = 3
print(longestSubsequence(arr, difference))