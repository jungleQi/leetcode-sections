#coding=utf-8

'''
We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].
Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.
(A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.
It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation:
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
'''

def minSwap(A, B):
    # n1 (natural1), the cost of making the first i columns increasing and not swapping the i-th column;
    # s1 (swapped), the cost of making the first i columns increasing and swapping the i-th column.
    r1, s1 = 0, 1

    N = len(A)
    for i in range(1, N):
        r2 = s2 = float("inf")

        #很容易陷入复杂的各种分支判断，陷入思维的细节不能自拔：
        #后来发现，可以归纳为两种情况：A[i], B[i] 不需要做交换 和 必须做交换
        # 1.本来不需要交换：stepA && stepB, 两步是为了获取当前index-i下的natural 和 swap的最小值
        # 2.需要做交换：stepA不会执行，按照前提,stepB是一定会执行的(It is guaranteed that the given input always makes it possible)

        #stepA
        if A[i - 1] < A[i] and B[i - 1] < B[i]:
            r2 = r1
            s2 = s1 + 1
        #stepB
        if A[i - 1] < B[i] and B[i - 1] < A[i]:
            r2 = min(r2, s1)
            s2 = min(s2, r1 + 1)

        r1, s1 = r2, s2

    return min(r1, s1)

A = [0,3,5,8,9]
B = [2,1,4,6,9]
print minSwap(A, B)