class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def subsets(nums):
    def helper(nums, cur, ret):
        ret.append(cur)

        if not nums: return
        for i,num in enumerate(nums):
            helper(nums[i+1:], cur+[num], ret)

    ret = []
    helper(nums, [], ret)
    return ret

nums = [1,2,3]
print(subsets(nums))