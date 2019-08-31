def partition(s):
    solutions = []
    sLen = len(s)

    def isParlin(subStr):
        right = len(subStr)-1
        left = 0
        while left < right:
            if subStr[left] != subStr[right]:
                return False
            left += 1
            right -= 1
        return True

    def travel(leftidx, curidx, accRes):
        if leftidx == sLen:
            solutions.append(accRes)
            return
        if curidx == sLen:
            return

        for rightidx in range(curidx+1, sLen+1):
            curStr = s[leftidx:rightidx]
            if isParlin(curStr):
                travel(rightidx, rightidx, accRes+[curStr])

    travel(0, 0, [])
    return solutions

print(partition(""))
