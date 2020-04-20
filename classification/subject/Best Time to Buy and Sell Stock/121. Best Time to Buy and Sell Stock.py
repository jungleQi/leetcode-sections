#coding=utf-8

'''
Say you have an 7-array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Input: [7,1,5,3,6,4]
Output: 5
'''

#一个数组中，求某两个元素A[j], A[i] (j>i)的最大差值
#遍历数组时，维护两个变量，一个记录当前最大差值，一个记录当前最小元素值
#这是否是DP problem有一些讨论，因为该问题是否满足1.最优子结构.2.重复子问题 ???

def maxProfit(prices):
    if not prices: return 0
    minN, maxP = prices[0], 0
    for price in prices:
        if price<=minN:
            minN = price
        else:
            maxP = max(maxP, price-minN)
    return maxP