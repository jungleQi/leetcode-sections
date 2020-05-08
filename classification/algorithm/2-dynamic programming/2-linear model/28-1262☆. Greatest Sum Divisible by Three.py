#coding=utf-8
'''
Given an 7-array nums of integers, we need to find the maximum possible sum of elements
 of the 7-array such that it is divisible by three.
'''


def maxSumDivThree_complex(nums):
    dp = [0] * 3
    maxSum = 0
    for n in nums:
        if n <= 0: continue
        newdp = dp[:]
        for i in range(3):
            if dp[i] > 0:
                #若n = 2, dp[2] <- dp[0] ， ... ，dp[1] <- dp[2]
                # dp[2]被修改过，又赋值给dp[1]
                # 也就是在一轮循环中，dp[i]可能被叠加造成污染，赋值给后面的dp[j](j>i)，导致结果错误
                newdp[(i + n) % 3] = max(dp[i] + n, dp[(i + n) % 3])
        newdp[n % 3] = max(newdp[n % 3], n)
        dp = newdp[:]
        maxSum = max(dp[0], maxSum)
    return maxSum

def maxSumDivThree_concise(nums):
    seen = [0,0,0]
    for num in nums:
        # seen在循环体内被改变，这里需要预先复制一份，
        # 如果不复制，会导致后续i，取的是新计算出来，而不是原有的值
        for i in seen[:]:
            seen[(i+num)%3] = max(seen[(i+num)%3], i+num)
    return seen[0]

nums = [1,2,3,4,4]
print(maxSumDivThree_concise(nums))

'''
1.每个位置，对应三种状态：余0、余1、余2的最大和
'''