#coding=utf-8
from utils import Node
from utils import ListNode
import heapq
import collections

# [2,7,9,3,1]
def nthUglyNumber(n):
    i2,i3,i5 = 0,0,0
    ans = [1,]
    for i in range(1,n):
        ugly = min(ans[i2]*2, ans[i3]*3, ans[i5]*5)
        ans.append(ugly)
        if ugly == ans[i2]*2:
            i2 += 1
        if ugly == ans[i3]*3:
            i3 += 1
        if ugly == ans[i5]*5:
            i5 += 1

    return ans[-1]

print nthUglyNumber(10)