#time complexity is O(n²)
def maxProfit(prices):
    N = len(prices)
    dp = [0]*(N+1)
    for i in range(2,N+1):
        for j in range(1,i):
            if prices[j]<prices[i]:
                dp[i] = max(dp[i], dp[j-2])
    return dp[-1]

def maxProfit_sell_cooldown(prices):
    N = len(prices)
    sell = [0]*N
    cooldown = [0]*N

    sell[1] = prices[1]-prices[0]
    for i in range(2,N):
        #difficult to understand
        sell[i] = prices[i]-prices[i-1]+max(sell[i-1],cooldown[i-2])
        #easy to understand
        cooldown[i] = max(sell[i-1], cooldown[i-1])

    return max(cooldown[-1], sell[-1])

#more easy to understand
def maxProfit_hold_cash(prices):
    N = len(prices)
    cash = [0]*N
    hold = [0]*N #must have share in hand

    hold[0] = -prices[0]
    for i in range(1,N):
        cash[i] = max(cash[i-1], prices[i] + hold[i-1])
        hold[i] = max(hold[i-1], (cash[i-2] if i>1 else 0)-prices[i])

    return cash[-1]

prices = [6,5,4,3]
print(maxProfit_hold_cash(prices))


