def maximumSum(arr):
    N = len(arr)
    dp1 = [0]*N
    dp2 = [0]*N

    maxSum = arr[0]
    dp1[0] = arr[0]
    for i in range(1,N):
        dp1[i] = (dp1[i-1]+arr[i]) if dp1[i-1]>0 else arr[i]
        maxSum = max(maxSum, dp1[i])

    dp2[N-1] = arr[N-1]
    for i in range(N-2, -1, -1):
        dp2[i] = (dp2[i+1]+arr[i]) if dp2[i+1]>0 else arr[i]

    for i in range(1,N-1):
        if arr[i] < 0:
            maxSum = max(maxSum, dp1[i-1]+dp2[i+1])

    return maxSum

arr = [8,-1,6,-7,-4,5,-4,7,-6]
print(maximumSum(arr))

#case 1, we don't delete anything, which can be solved by max subarray problem
#case 2, we only delete one element.
#dp1 to store the max subarray ended with positive i. dp2 to store max subarray started at positive i.