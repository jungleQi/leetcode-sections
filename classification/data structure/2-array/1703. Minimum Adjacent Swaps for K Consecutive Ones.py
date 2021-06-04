'''
You are given an integer array, nums, and an integer k.
nums comprises of only 0's and 1's. In one move, you can choose two adjacent indices and swap their values.

Return the minimum number of moves required so that nums has k consecutive 1's.


Example 1:
Input: nums = [1,0,0,1,0,1], k = 2
Output: 1
Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive 1's.

Example 2:
Input: nums = [1,0,0,0,0,0,1,1], k = 3
Output: 5
Explanation: In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,1,1,1].
'''

def minMoves(nums, k):
    if k == 1:
        return 0

    g, total, count = list(), [0], -1
    for i, num in enumerate(nums):
        if num == 1:
            count += 1

            #nums[i]在前面i-1个1全部左移相连后，需要移动多少距离 才能贴着前面的1
            g.append(i - count)

            total.append(total[-1] + g[-1])

    m, ans = len(g), float("inf")

    for i in range(m - k + 1):
        mid = (i + i + k - 1) // 2
        q = g[mid]
        #计算公式可以推演得到
        ans = min(ans, (2 * (mid - i) - k + 1) * q + (total[i + k] - total[mid + 1]) - (total[mid] - total[i]))

    return ans