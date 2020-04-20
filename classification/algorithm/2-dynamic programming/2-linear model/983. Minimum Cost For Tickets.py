import sys
def mincostTickets(days, costs):
    dp = {}
    dp[0] = 0
    for i in range(1,366):
        if i in days:
            dp[i] = min(dp[i-1]+costs[0], dp[max(0,i-7)]+costs[1], dp[max(0, i-30)]+costs[2])
        else:
            dp[i] = dp[i-1]

    return dp[365]

days =[1,4,6,7,8,40]
costs =[2,7,15]
print mincostTickets(days, costs)