'''
Given a square 7-array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.
The next row's choice must be in a column that is different from the previous row's column by at most one.
'''

def minFallingPathSum(A):
    N = len(A)
    while len(A) >= 2:
        row = A.pop()
        for i in range(N):
            A[-1][i] += min(row[max(0,i-1):min(N,i+2)])
    return min(A[0])

A = [[17,82],[1,-44]]
print(minFallingPathSum(A))