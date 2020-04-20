'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''

def climbStairs(n):
    f1,f2 = 1,0
    for i in range(n):
        f2,f1 = f1, f1+f2
    return f1

print(climbStairs(0))

