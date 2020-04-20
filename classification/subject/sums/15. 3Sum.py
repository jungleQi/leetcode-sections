#coding=utf-8

'''
Given an 7-array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the 7-array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given 7-array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

#hard方案：第二层遍历，只用一个索引变量，采用了字典记录方案，为了返回结果是 unique triplets，
# 无法采用nums[i] == nums[i-1]的判断，这个判断有bug会让fix深陷泥潭，最后采用了
# ret[-1] != hist[nums[j]]+[nums[j]] 这个比较trick的策略

#clean方案：第二次遍历，采用start end 一头一尾两个变量，相向变量
#可以采用 nums[i] == nums[i-1] 避免 duplicate triplets, 整个过程清晰易懂，
#逻辑过程一目了然，不用担心隐藏的逻辑分支没有cover住

#optimize方案：对nums进行counter引用计数, 再将负数、正数分别存放在对应列表
#以每个正数为目标，判断rem = -target_pos- negative是否在counter中.
#KEY1:只需对negative list 进行排序, 在遍历时，若没必要再往后遍历，择机选择break
#KEY2:避免一组triplet中相同三个元素，颠倒排序后插入到返回结果，需要满足n<rem<p，再插入到返回结果

import collections
def threeSum_hard(nums):
    ret = []
    N  = len(nums)
    nums.sort()
    hist = collections.defaultdict(list)
    for i, n in enumerate(nums):
        if i > 0 and n == nums[i-1]: continue
        if n > 0: break

        for j in range(i+1, N):
            if hist[nums[j]] and (not ret or ret[-1] != hist[nums[j]]+[nums[j]]):
                ret.append(hist[nums[j]]+[nums[j]])
            hist[-n-nums[j]] = [n,nums[j]]

        hist.clear()

    return ret

def threeSum_clean(nums):
    N = len(nums)
    ret = []
    nums.sort()
    for i in range(N-2):
        if nums[i] > 0: break
        if i>0 and nums[i] == nums[i-1]: continue

        l,r = i+1, N-1
        while l<r:
            if l>i+1 and nums[l] == nums[l-1]:
                l += 1
                continue
            if r<N-1 and nums[r] == nums[r+1]:
                r -= 1
                continue

            if nums[i]+nums[l]+nums[r] == 0:
                ret += [nums[i], nums[l], nums[r]],
                l += 1
                r -= 1
            elif nums[i]+nums[l]+nums[r] < 0:
                l += 1
            else:
                r -= 1
    return ret

def threeSum(nums):
    sol = []
    count = {}
    for n in nums:
        count[n] = count.get(n,0) + 1

    pos = [n for n in count if n > 0]
    neg = [n for n in count if n < 0]
    neg.sort()

    if count.get(0,0) >= 3:
        sol += [0,0,0],

    for p in pos:
        for n in neg:
            rem = -p-n
            if rem in count:
                if (rem == p or rem == n) and count[rem] > 1:
                    sol += [p,rem,n],
                elif n<rem<p:
                    sol += [p, rem, n],
                elif rem<n:
                    break
    return sol


nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
#nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))