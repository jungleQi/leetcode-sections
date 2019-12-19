'''
Given a collection of distinct integers, return all possible permutations.
'''

def permute(nums):
    def _helper(nums, i, path, ret):
        if i == 0:
            ret += path,
            return

        for n in nums:
            if n in path: continue
            _helper(nums, i-1, path+[n], ret)

    ret = []
    _helper(nums, len(nums), [], ret)
    return ret

nums = [1,2,3]
print(permute(nums))