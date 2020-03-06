def minSwap(A, B):
    swapRecord, fixRecord = 1, 0
    for i in range(1, len(A)):
        if A[i-1]>=B[i] or B[i-1] >= A[i]:
            swapRecord += 1
        elif A[i-1]>=A[i] or B[i-1]>=B[i]:
            temp = swapRecord
            swapRecord = fixRecord+1
            fixRecord = temp
        else:
            minval = min(swapRecord, fixRecord)
            fixRecord = minval
            swapRecord = minval+1

    return min(swapRecord, fixRecord)

A = [0,3,5,8,9]
B = [2,1,4,6,9]
print minSwap(A, B)