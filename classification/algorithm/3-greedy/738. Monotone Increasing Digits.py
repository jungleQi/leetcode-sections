'''
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9

Input: N = 332
Output: 299
'''

def monotoneIncreasingDigits_III(n):
    numstr = str(n)
    N = len(numstr)
    i = 0
    #正向遍历找到第一个下降的跳点
    while i < N - 1:
        if numstr[i] > numstr[i + 1]:
            break
        i += 1
    if i == N - 1: return n

    #从跳点反向遍历，找到第一个可以自减1(满足monotone increasing)的点
    while i > 0:
        if numstr[i] != numstr[i - 1]: break
        i -= 1
    return int(numstr[:i] + str(int(numstr[i]) - 1) + '9' * (N - i - 1))


def monotoneIncreasingDigits_II(N):
    digStr = list(str(N))
    start = 0
    for i in range(1, len(digStr)):
        if digStr[i]>digStr[i-1]:
            start = i
        elif digStr[i]<digStr[i-1]:
            break

    if start == len(digStr)-1:
        return N
    else:
        if digStr[start] == '1':
            return int('9'*(len(digStr)-start-1))
        else:
            digStr[start] = str(int(digStr[start])-1)
            return int("".join(digStr[:start+1]) + '9'*(len(digStr)-start-1))


def monotoneIncreasingDigits_I(N):
    arr = [int(c) for c in str(N)]
    nLen = len(arr)

    curidx,latestConvertIdx = 0, nLen
    for curidx in range(nLen-2, -1, -1):
        if arr[curidx] > arr[curidx+1]:
            latestConvertIdx = curidx+1
            arr[curidx] = arr[curidx]-1

    resArr = [9]*(nLen-latestConvertIdx)
    if arr[curidx] != 0:
        res = arr[:latestConvertIdx] + resArr
    else:
        res = resArr

    ret = [str(i) for i in res]
    return int("".join(ret)) if ret else 0

N = 2220 #101
print(monotoneIncreasingDigits(N))