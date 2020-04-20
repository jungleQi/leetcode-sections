def firstMissingPositive(nums):
    n = len(nums)
    A = [0]*n

    for num in nums:
        if 1<=num<=n:
            A[num-1] = 1

    for idx, i in enumerate(A):
        if i == 0:
            return idx+1
    return n+1

nums = [3,2,0]
print(firstMissingPositive(nums))