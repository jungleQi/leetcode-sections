class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def permuteUnique_fast(nums):
    def helper(nums, cur, ret):
        if not nums:
            ret.append(cur)
            return

        for i,num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            helper(nums[:i]+nums[i+1:], cur+[num], ret)

    nums.sort()
    ret = []
    helper(nums, [], ret)
    return ret