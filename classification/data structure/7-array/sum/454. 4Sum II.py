def fourSumCount(A, B, C, D):
    hashTbl = {}
    for a in A:
        for b in B:
            sum = a+b
            if sum in hashTbl:
                hashTbl[sum] += 1
            else:
                hashTbl[sum] = 1

    count = 0
    for c in C:
        for d in D:
            sum = -(c+d)
            if sum in hashTbl :
                count += hashTbl[sum]

    return count

A = [ 1, 2, -1]
B = [-2,-1,-1]
C = [-1, 2,1]
D = [ 0, 2,1]
print(fourSumCount(A,B,C,D))