import collections
def longestSubsequence(arr, difference):
    dp = collections.defaultdict(lambda :0)
    maxLen = 1
    for i in arr:
        dp[i] = dp[i-difference]+1
        maxLen = max(maxLen, dp[i])

    return maxLen

def longestSubsequence_LTE(arr, difference):
    N = len(arr)
    dp = [1] * N

    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            dist = arr[i] - arr[j]
            if dist != difference:
                continue

            if dist == difference:
                dp[i] = dp[j] + 1
            elif dist == 0:
                dp[i] = dp[j]
            break
    return max(dp)

arr = [1]
#arr = [1,5,7,8,5]
difference = 3
print(longestSubsequence(arr, difference))