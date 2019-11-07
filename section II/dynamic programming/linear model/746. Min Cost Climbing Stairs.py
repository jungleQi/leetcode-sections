'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor,
and you can either start from the step with index 0, or the step with index 1.
'''

#[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
def minCostClimbingStairs(cost):
    f1, f2 = 0, 0
    for x in cost:
        f1,f2 = min(f1,f2)+x,f1

    return min(f1,f2)

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))

