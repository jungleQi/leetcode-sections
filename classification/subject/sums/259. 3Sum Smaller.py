#coding=utf-8

'''
Given an 2-array of n integers nums and a target, find the number of index triplets i, j, k
with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
'''

#第二层循环采用l,r两个变量广泛应用于triplet问题
#进入第二层循环之前，对两种特殊的case进行处理，能避免进入二层循环

def threeSumSmaller(nums, target):
    ans, N = 0, len(nums)
    nums.sort()
    for i in range(N-2):
        l,r = i+1,N-1
        if nums[i]+nums[l]+nums[l+1]>target:
            break
        elif nums[i]+nums[r-1]+nums[r]<target:
            #容易弄错起算边界和高
            ans += (N-i-2)*(N-i-1)/2
        else:
            while l<r:
                cursum = nums[i]+nums[l]+nums[r]
                if cursum<target:
                    ans += r-l
                    l += 1
                else:
                    r -= 1
    return ans

target = 20
nums = [-4,-2,-2,0,1,1,2,3,3,4,5]

print(threeSumSmaller(nums, target))