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
    graph = collections.defaultdict(list)
    N = len(arr)
    for i in range(N):
        if i+arr[i]<N:
            graph[i].append(i+arr[i])
        if i-arr[i]>=0:
            graph[i].append(i-arr[i])

    deque = collections.deque([start])
    visitor = set()
    while deque:
        idx = deque.popleft()
        if arr[idx] == 0:
            return True

        visitor.add(idx)
        for i in graph[idx]:
            if i in visitor: continue
            deque.append(i)
    return False

arr = [0]
start = 0
print(canReach(arr, start))