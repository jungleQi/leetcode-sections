#coding=utf-8

'''
Given an array A of positive integers, call a (contiguous, not necessarily distinct)
subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers:
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
'''

#当新元素加入时，保证窗口内不同元素的个数不超过K，收缩窗口(确定窗口左边边界)的办法有多种
#native:1.用dict维护窗口内的元素及个数，以左边界为起始点开始遍历，如果该元素只有一个，
#       该元素右边的元素为新的左边界；如果该元素不止一个，继续往右遍历，直到找到只有
#       一个数量的元素。
#       2.基于新的左边界和当前元素作为右边界，计算这个新窗口区间里的，以当前元素为终点的
#       子区间的不同元素个数为K的区间数

#grace: 1.子区间不同元素为K的区间数，以当前元素为右边界，
#       不同元素为K的区间数=不同元素为K个的左边界索引值 - 不同元素为K-1个的左边界索引值
#       2.通过1的算法，可以抽象出窗口滑动函数，满足K 和 K-1的左边界确定
#       3.为了更好的满足窗口滑动，为了保证dict元素和区间元素严格对应，频繁的del/add，不是
#       能够很方便的管理访问过的元素，采用计数的方式，会非常优雅方便
#       4.基于2，3分析，创建一个window类，可以在访问新元素后，很好的按照预期进行滑窗

import collections

class Window:
    def __init__(self):
        self.count = collections.Counter()
        self.nonzero = 0

    def add(self, x):
        self.count[x] += 1
        if self.count[x] == 1:
            self.nonzero += 1

    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.nonzero -= 1


def subarraysWithKDistinct(A, K):
    win1 = Window()
    win2 = Window()

    ans = left1 = left2 = 0
    for right, x in enumerate(A):
        win1.add(x)
        win2.add(x)
        while win1.nonzero > K:
            win1.remove(A[left1])
            left1 += 1

        while win2.nonzero >= K:
            win2.remove(A[left2])
            left2 += 1

        ans += left2-left1

    return ans

A = [1,2,1,2,3]
K = 2
print(subarraysWithKDistinct(A, K))