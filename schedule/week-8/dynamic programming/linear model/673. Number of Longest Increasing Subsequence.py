import collections
def findNumberOfLIS(nums):
    N = len(nums)
    lens = [0]*N
    counts = [1]*N

    for i,num in enumerate(nums):
        for j in range(i):
            if nums[j]<nums[i]:
                if lens[j] >= lens[i]:
                    lens[i] = lens[j] + 1
                    counts[i] = counts[j]
                elif lens[j]+1 == lens[i]:
                    counts[i] += counts[j]

    maxlen,res = 0,0
    for i,length in enumerate(lens):
        if length > maxlen:
            res = counts[i]
            maxlen = length
        elif length == maxlen:
            res += counts[i]

    return res

nums = [1,3,5,4,3,4]
#nums = [1,3,5,4,7]
print(findNumberOfLIS(nums))