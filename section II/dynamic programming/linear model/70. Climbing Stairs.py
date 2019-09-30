def climbStairs(n):
    prev_1, prev_2 = 2, 1
    sumer = 1 if n<=1 else 2

    for i in range(2,n):
        sumer = prev_1 + prev_2
        prev_2, prev_1 = prev_1, sumer
    return sumer

n = 1
print climbStairs(n)