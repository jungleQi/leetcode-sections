def find132pattern(nums):
    minidx = []
    for num in nums:
        if not minidx or num < minidx[-1]:
            minidx += num,
        else:
            minidx += minidx[-1],

    stack = []
    i = 0
    for num in reversed(nums):
        i -= 1
        if minidx[i] == num:
            continue

        if not stack or num<stack[-1]:
            stack += num,
            continue

        while stack and (stack[-1]<=minidx[i] or stack[-1]==num):
            stack.pop()

        if stack and num>stack[-1] and minidx[i]<stack[-1]:
            return True

        stack += num,

    return False

nums = [-2,1,1,-2,1,2]
#nums = [-2,1,1]
#nums = [3,5,0,3,4]
print find132pattern(nums)