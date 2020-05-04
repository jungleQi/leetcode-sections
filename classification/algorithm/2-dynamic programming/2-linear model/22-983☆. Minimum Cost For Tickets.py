#coding=utf-8

'''
In a country popular for train travel, you have planned some train travelling one year in advance.
The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:
    1.a 1-day pass is sold for costs[0] dollars;
    2.a 7-day pass is sold for costs[1] dollars;
    3.a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.
For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
'''

#lightspot:
# 1.表面上给定的是days包含的几个阶段，但便于推理，将实际处理的阶段扩展成 [1 ... 366]
# 2.dp[max(0,i-7)]+costs[1] 索引值的设定采用max(0,i-7)，避免越过边界. 如果用if else就没这么优雅

def mincostTickets(days, costs):
    everydays = [0] * 366
    dp = [0] + [float("inf")] * 365
    costmap = {costs[0]: 1, costs[1]: 7, costs[2]: 30}
    for day in days:
        everydays[day] = 1

    for i in range(1, 366):
        if everydays[i] == 0:
            dp[i] = dp[i - 1]
            continue

        for cost, step in costmap.items():
            if i - step >= 0:
                dp[i] = min(dp[i], dp[i - step] + cost)
            else:
                dp[i] = min(dp[i], cost)
    return dp[-1]

def mincostTickets_concise(days, costs):
    dp = {}
    dp[0] = 0
    for i in range(1,366):
        if i in days:
            #非常优雅
            dp[i] = min(dp[i-1]+costs[0], dp[max(0,i-7)]+costs[1], dp[max(0, i-30)]+costs[2])
        else:
            dp[i] = dp[i-1]

    return dp[365]

days =[1,4,6,7,8,40]
costs =[2,7,15]
print mincostTickets(days, costs)