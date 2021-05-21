'''
Given an array of non-negative integers arr, you are initially positioned at start index of the array.
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3
'''

import collections
def canReach(arr, start):
    q = collections.deque()

    #！！！！ 此处vistor用数组的方式非常高效，如果用set进行检索判断，会让效率下降很多
    visited = [0] * len(arr)
    visited[start] = 1
    q.append(start)

    while q:
        pos = q.popleft()
        if arr[pos] == 0:
            return True
        left = pos - arr[pos]
        right = pos + arr[pos]
        if right < len(arr) and not visited[right]:
            q.append(right)
            visited[right] = 1
        if left >= 0 and not visited[left]:
            q.append(left)
            visited[left] = 1

    return False


arr = [4,2,3,0,3,1,2]
start = 2
print(canReach(arr, start))