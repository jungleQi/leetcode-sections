import collections

class Window():
    def __init__(self):
        self.nonzero = 0
        self.counter = collections.Counter()

    def add(self, num):
        self.counter[num] += 1
        if self.counter[num] == 1:
            self.nonzero += 1

    def remove(self, num):
        self.counter[num] -= 1
        if self.counter[num] == 0:
            self.nonzero -= 1


class solution(object):
    def subarraysWithKDistinct(self, A, K):
        win1 = Window()
        win2 = Window()

        ans, left1, left2 = 0, 0, 0
        for idx, num in enumerate(A):
            win1.add(num)
            win2.add(num)

            while win1.nonzero > K:
                win1.remove(A[left1])
                left1 += 1

            while win2.nonzero >= K:
                win2.remove(A[left2])
                left2 += 1

            ans += left2 - left1

        return ans


A = [1,1]
K = 1
obj = solution()
print obj.subarraysWithKDistinct(A,K)
