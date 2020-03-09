
'''
Time complexity : O(N!). There is N possibilities to put the first queen, not more than N (N - 2) to put the second one,
not more than N(N - 2)(N - 4) for the third one etc. In total that results in O(N!) time complexity.
'''

import copy
def solveNQueens(n):
    def isAttack(layout, curCol):
        M = len(layout)
        for row in range(M):
            for i in range(1,M+1):
                if (curCol-i >=0 and curCol-i == layout[M-i]) or (curCol+i<n and curCol+i == layout[M-i]):
                    return True
            if curCol == layout[row]:
                return True
        return False

    def helper(row, layout, ret):
        if row == n:
            ret.append(layout)
            return

        for col in range(n):
            if isAttack(layout, col):
                continue
            helper(row+1, layout+[col], ret)

    ret = []
    helper(0, [], ret)

    ans = []
    for item in ret:
        curans = [ '.'*i+'Q'+'.'*(n-i-1) for i in item ]
        ans.append(curans)

    return ans

print(solveNQueens(4))