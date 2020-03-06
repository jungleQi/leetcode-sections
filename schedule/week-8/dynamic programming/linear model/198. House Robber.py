'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
'''

def rob(nums):
    f1,f2 = 0,0
    for num in nums:
        f2, f1 = f1, max(f2+num, f1)
    return f1

nums = [1,2]
print(rob(nums))
