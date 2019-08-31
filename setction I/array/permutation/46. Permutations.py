def permute(nums):
    def helper(nums, N, visitor, result, cnt, results):
        if cnt == N:
            results += result,
            return

        for num in nums:
            if num not in visitor:
                visitor.append(num)
                helper(nums, N , visitor, result+[num], cnt+1, results)
                visitor.pop()

    N = len(nums)
    results = []
    helper(nums, N, [], [], 0, results)
    return results

nums = [1,2,3]
print(permute(nums))
