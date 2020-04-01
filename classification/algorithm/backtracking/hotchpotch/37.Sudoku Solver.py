#coding=utf-8

'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
1.Each of the digits 1-9 must occur exactly once in each row.
2.Each of the digits 1-9 must occur exactly once in each column.
3.Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
'''

#backtracking的框架没有太多变化：
#1. 判断返回：
#   1.1 如果'.'全部都替换完毕，就返回
#   1.2 如果递归函数返回True，就层层向上返回True，可以结束整个递归树;如果返回False，就continue ,执行与之平行的另一个子节点的递归树

#2.pruning:
#   2.1 如果当前准备填充的数字不满足条件(行、列、小格子有重复的数字)，就不用展开子递归树

#但是沿用原有的数据结构来判断[2.1]，就会比较慢。
# --> 需要将原有9*9的数据结构转换成row、column、box都为hash结构的dict，便于快速查找字符

import collections
def solveSudoku(board):
    def could_place(num, row, col):
        """
        Check if one could place a number d in (row, col) cell
        """
        return not (num in rows[row] or num in columns[col] or \
                    num in boxes[box_index(row, col)])

    def place_number(d, row, col):
        """
        Place a number d in (row, col) cell
        """
        rows[row][d] += 1
        columns[col][d] += 1
        boxes[box_index(row, col)][d] += 1
        board[row][col] = d

    def remove_number(d, row, col):
        """
        Remove a number which didn't lead
        to a solution
        """
        del rows[row][d]
        del columns[col][d]
        del boxes[box_index(row, col)][d]
        board[row][col] = '.'

    def travel(idx):
        if idx == fillCount :
            return True

        for n in range(1, 10):
            if not could_place(str(n), fillCoord[idx][0], fillCoord[idx][1]):
                continue

            place_number(str(n), fillCoord[idx][0], fillCoord[idx][1])
            if not travel(idx+1):
                remove_number(str(n), fillCoord[idx][0], fillCoord[idx][1])
            else:
                return True

        return False

    # box size
    n = 3
    # row size
    N = n * n
    # lambda function to compute box index
    box_index = lambda row, col: (row // n) * n + col // n

    fillCount = 0
    # init rows, columns and boxes
    rows = [collections.defaultdict(int) for i in range(N)]
    columns = [collections.defaultdict(int) for i in range(N)]
    boxes = [collections.defaultdict(int) for i in range(N)]
    fillCoord = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != '.':
                d = board[i][j]
                place_number(d, i, j)
            else:
                fillCoord.append([i,j])
                fillCount += 1

    travel(0)

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solveSudoku(board)
print(board)