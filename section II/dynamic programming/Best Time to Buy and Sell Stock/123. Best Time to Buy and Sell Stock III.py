#coding=utf-8

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Input: [3,3,5,0,0,3,1,4]
Output: 6
'''

'''
native版本 ERROR: 
0.遍历得到连续递增序列，利用这个递增序列首尾值得到这个区间的Profit，放入list。排序list得到最大的两个profit，两者的和就是最大收益。
这个解法的问题是，假设有两个最大收益区间A [1,5,4,9]不是递增，获得最大收益是8，被以上规则拆分成 4, 5。若有多个类似区域，
最后从拆解后的较小数中选择，自然不是想要的结果，出现ERROR

正确版本TLE:
1.dp[k][i] represents the max profit up until prices[ii] (Note: NOT ending with prices[ii]) using at most k transactions. 
2.判断第i天交易，可获得的最大利润，状态转移方程为：
    dp[k][i] = max(dp[k][i-1], dp[k-1][j]+prices[i]-prices[j]), 其中j = [1..i],需要循环执行
    如果嵌套循环[1..i]，求max(dp[k-1][j] - prices[j])，会出现TLE

优化版本 PASS:
3.改进之后：dp[k][i] = max(dp[k][i-1], prices[i] + max(dp[k-1][j] - prices[j])) 其中j = [1..i]
  该方程按照交易逻辑是比较难以直接理解，但是在按照自然交易逻辑，变换之后的这个方程，放在程序的迭代中，又是比较好理解的
  
改进版本的关键：对常规思路得出的方程，提取出循环中不变的变量，得出新的方程，这个方程按照一般思路难以直接得到，但是通过简单
变换，得到的这个新方程，只需要在两层遍历，就能完成迭代
'''

def maxProfit_TLE(prices):
    K, N = 2, len(prices)
    dp = [[0] * N for _ in range(K)]
    for k in range(K):
        for i in range(N):
            max_profit = -1
            for j in range(i):
                max_profit = max(max_profit, dp[k - 1][j] + prices[i] - prices[j])
            dp[k][i] = max(dp[k][i - 1], max_profit)
    return dp[-1][-1]

def maxProfit(prices):
    K, N = 2, len(prices)
    dp = [[0]*N for _ in range(K)]
    for k in range(K):
        max_profit = -prices[0]
        for i in range(1,N):
            max_profit = max(dp[k-1][i-1]-prices[i-1], max_profit)
            dp[k][i] = max(dp[k][i-1], max_profit + prices[i])

    return dp[-1][-1]



nums = [1,2,4,2,5,7,2,4,9,0]
print(maxProfit(nums))