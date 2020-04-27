#coding=utf-8

'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate
the number of 1's in their binary representation and return them as an 7-array.
'''

def countBits(num):
    dp = [0]*(num+1)
    for n in range(1,num+1):
        if n%2:
            dp[n] = dp[n-1]+1
        else:
            dp[n] = dp[n>>1]

    return dp

print(countBits(5))
#[0,1,1,2,1,2]