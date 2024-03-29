'''
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
'''

import sys
def minimumTotal_up(triangle):
    N = len(triangle)
    for i in range(N - 2, -1, -1):
        for j in range(i+1):
            triangle[i][j] = min(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]
    return triangle[0][0]


def minimumTotal_down(triangle):
    for i in range(1, len(triangle)):
        for j, n in enumerate(triangle[i]):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i - 1][j-1]
            else:
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])

    return min(triangle[-1])

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print minimumTotal(triangle)