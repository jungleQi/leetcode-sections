def kConcatenationMaxSum(arr, k):
    def get_max_sub(a):
        maxsum = cursum = 0
        for v in a:
            cursum += v
            if cursum < 0:
                cursum = 0 if v < 0 else v
            else:
                maxsum = max(maxsum, cursum)

        return maxsum

    if max(arr) <= 0: return 0
    max1 = get_max_sub(arr)
    max2 = get_max_sub(arr*2)

    max3 = sum(arr)
    if max3>0 and k>2:
        max3 = (k-2)*max3 + max2

    return max(max1,max2,max3) % (10**9 + 7)

arr = [1,-2,1]
k = 5
print kConcatenationMaxSum(arr, k)