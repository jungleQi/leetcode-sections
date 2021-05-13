import collections

def nextGreaterElements(nums):
    stack = []
    N = len(nums)
    ret = [-1]*N

    for i,num in enumerate(nums+nums):
        while stack and nums[stack[-1]]<num:
            ret[stack[-1]] = num
            stack.pop()
        if(i<N):
            stack.append(i)

    return ret

nums = [2,1]
print(nextGreaterElements(nums))