'''

The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

'''

#time complexity: O((n**3)!)  can be optimized to O(n!)

def totalNQueens(n):
    def isPossible(layout, curCol):
        M = len(layout)
        for row in range(M):
            for i in range(1, M + 1):
                if (curCol - i >= 0 and curCol - i == layout[M - i]) or (
                        curCol + i < n and curCol + i == layout[M - i]):
                    return True
            if curCol == layout[row]:
                return True
        return False

    def helper(layout, remainRow, ret):
        if remainRow == 0:
            ret[0] += 1
            return
        for col in range(n):
            if isPossible(layout, col): continue
            helper(layout+[col], remainRow-1, ret)

    ret = [0]
    helper([], n, ret)
    return ret[0]

print(totalNQueens(2))