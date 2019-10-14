import sys
def findTargetSumWays(nums, S):
    def _cal(nums, N, i, curSum, memo):
        if i == N:
            if curSum == S:
                return 1
            else:
                return 0
        elif memo[i][curSum+1000] != -sys.maxint:
            return memo[i][curSum+1000]
        else:
            add = _cal(nums, N, i+1, curSum+nums[i], memo)
            subtract =  _cal(nums, N, i + 1, curSum-nums[i], memo)
            memo[i][curSum+1000] = add+subtract
            return memo[i][curSum+1000]

    N = len(nums)
    memo = [[-sys.maxint for _ in range(2001)] for _ in range(N)]
    return _cal(nums, N, 0, 0, memo)

nums = [2,20,24,38,44,21,45,48,30,48,14,9,21,10,46,46,12,48,12,38]
S = 48
#nums = [1, 1, 1, 1, 1]
#S = 3
print(findTargetSumWays(nums, S))