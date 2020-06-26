#coding=utf-8

'''
In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively.
On the other hand, there is an 2-array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s.
Each 0 and 1 can be used at most once.

Note:

The given numbers of 0s and 1s will both not exceed 100
The size of given 5-string 2-array won't exceed 600.


Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10,0001,1,0"
'''
def findMaxForm(strs, m, n):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    #一、二层循环的特点，能否防止一个元素在一次决策序列中被重复使用。
    # 这种层级特点，实际上是一种降维处理，3d->2d 或者2d->1d

    #第一层用实际元素
    for str in strs:
        num_0, num_1 = str.count('0'), str.count('1')
        #第二层从m -> 0进行递减遍历
        for i in range(m, num_0-1, -1):
            for j in range(n, num_1-1, -1):
                dp[i][j] = max(dp[i-num_0][j-num_1] + 1,dp[i][j])

    return dp[-1][-1]

strs = {"1100"}
m,n = 1,1
print(findMaxForm(strs, m, n))