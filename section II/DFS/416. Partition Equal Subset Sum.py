#coding=utf-8

def canPartition_dfs(nums):
    sumer = sum(nums)
    if sumer & 1 == 1:
        return False
    nums.sort(reverse=True)

    def dfs(index, target):
        if target == 0:
            return True
        if index == len(nums) or target < nums[index]:
            return False

        return dfs(index+1, target-nums[index]) or dfs(index+1, target)

    return dfs(0, sumer//2)

def canPartition(nums):
    

nums = [1,1]
print canPartition(nums)



