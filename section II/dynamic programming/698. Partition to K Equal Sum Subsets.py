def canPartitionKSubsets(nums, k):
    def helper(nums, N, start, k, cursum, target,  visitor):
        if k == 1: return True
        if cursum > target: return False
        if cursum == target: return helper(nums, N, 0, k-1, 0, target, visitor)

        for i in range(start, N):
            if visitor[i]: continue
            visitor[i] = 1
            if helper(nums, N, i+1, k, cursum+nums[i], target, visitor):
                return True
            visitor[i] = 0

        return False

    if sum(nums)%k != 0: return False

    N = len(nums)
    target = sum(nums)/k
    visitor = [0]*N
    return helper(nums, N, 0, k, 0, target, visitor)

#nums = [85,35,40,64,86,45,63,16,5364,110,5653,97,95]
#k = 7
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
print canPartitionKSubsets(nums, k)



