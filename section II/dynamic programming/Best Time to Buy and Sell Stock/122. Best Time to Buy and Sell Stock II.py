#coding=utf-8

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Input: [7,1,5,3,6,4]
Output: 7
'''

'''
最native的想法：
    遍历到当前值，判断如果当前元素比前一个大，就记录为当前最大值，继续增长。如果当前元素比前一个小，就马上计算前一个元素的
收益，并将当前元素记为新一个transactions的最小起点；
    这里有很多细节去处理，如果当前值不是下降挂点第一个值，而是连续下降值中的某个，那么会让上续判断变得复杂，需要额外增加一个
变量，记录是否是增长过程中的首次下降，根据这个变量状态，去做分支判断：是否开始计算收益，或者是否只做新transactions的最小起点更新

grace的想法：
    只要价格出现增长，就记录此次增长获得的收益，并入总的收益；如果价格是下降，就不做任何处理。最终累积的收益就是最大收益
'''

def maxProfit(prices):
    profitSum = 0
    i, N = 1,len(prices)
    while i < N:
        curprofit = prices[i]-prices[i-1]
        if curprofit > 0: profitSum += curprofit
        i += 1

    return profitSum

prices = [7]
print(maxProfit(prices))
