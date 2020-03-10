'''
Given a collection of distinct integers, return all possible permutations.
'''

#time complexity : O(n!)

def permute(nums):
    def helper(nums, comb, ret):
        if not nums:
            ret.append(comb)
            return

        for i, num in enumerate(nums):
            helper(nums[:i]+nums[i+1:], comb+[num], ret)

    ret = []
    helper(nums, [], ret)
    return ret

nums = [1,2,3]
print(permute(nums))