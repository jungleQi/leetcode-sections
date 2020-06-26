#coding=utf-8

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    rows = [{} for i in range(9)]
    cols = [{} for i in range(9)]
    #box分成9个单元，依次排列
    boxes = [{} for i in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                #对box的定位
                boxIdx = (i / 3) * 3 + j / 3
                rows[i][num] = rows[i].get(num, 0) + 1
                cols[j][num] = cols[j].get(num, 0) + 1
                boxes[boxIdx][num] = boxes[boxIdx].get(num, 0) + 1

                if rows[i][num] > 1 or cols[j][num] > 1 or boxes[boxIdx][num] > 1:
                    return False
    return True