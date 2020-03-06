def canPartitionKSubsets(nums, k):
    nums.sort()

    N = len(nums)
    target, mod = divmod(sum(nums), k)
    if mod != 0 or nums[-1]>target:
        return False

    dp = [0]*(1<<N)
    totalsum = [0]*(1<<N)

    dp[0] = True
    for i in range(1<<N):
        if dp[i]:
            for j in range(N):
                tmp = i|(1<<j)
                if tmp != i:
                    if nums[j] <= (target-totalsum[i]%target):
                        totalsum[tmp] = totalsum[i]+nums[j]
                        dp[tmp] = True
                    else:
                        break

    return dp[-1]

#nums = [1,2,2]
#print canPartitionKSubsets(nums, 2)

nums = [10,10,10,7,7,7,7,7,7,6,6,6]
k = 3
#nums = [4, 3, 2, 3, 5, 2, 1]
#k = 4
print canPartitionKSubsets(nums, k)



