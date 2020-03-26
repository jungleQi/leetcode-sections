'''
Given an array of scores that are non-negative integers.
 Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on.
 Each time a player picks a number, that number will not be available for the next player.
 This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner.
You can assume each player plays to maximize his score.
'''

def PredictTheWinner(nums):
    N = len(nums)
    dp = [[0] * N for _ in range(N)]

    for i in range(N - 1, -1, -1):
        if i == N - 1: dp[i][i] = nums[i]

        for j in range(i + 1, N):
            dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

    return dp[0][-1] >= 0

nums = [1, 5]
print(PredictTheWinner(nums))