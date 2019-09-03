def nextGreaterElements(nums):
    N = len(nums)
    next = [-1]*N
    stack = []
    for i in range(2*N):
        i = i%N
        while stack and nums[stack[-1]] < nums[i]:
            next[stack[-1]] = nums[i]
            stack.pop()

        if i<N:
            stack.append(i)

    return next

nums = [1,2,1]
print nextGreaterElements(nums)