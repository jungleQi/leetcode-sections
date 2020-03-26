import sys
def minimumTotal(triangle):
    N = len(triangle)
    for i in range(N - 2, -1, -1):
        for j in range(i+1):
            triangle[i][j] = min(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]
    return triangle[0][0]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print minimumTotal(triangle)