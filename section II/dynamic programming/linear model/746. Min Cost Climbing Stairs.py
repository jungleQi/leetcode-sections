def minCostClimbingStairs(cost):
    prev_1 = cost[1]
    prev_2 = cost[0]
    for val in cost[2:]:
        curMin = min(prev_2, prev_1) + val
        prev_2, prev_1 =  prev_1, curMin
    return min(prev_1, prev_2)

cost = [10, 15, 20]
print minCostClimbingStairs(cost)