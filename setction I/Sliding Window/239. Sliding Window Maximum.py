from collections import deque

def maxSlidingWindow(nums, k):
    if not nums:
        return []
    if k == 0:
        return nums

    result = []

    deq = deque()
    for i in range(k):
        while len(deq) > 0:
            if nums[deq[-1]] < nums[i]:
                deq.pop()
            else:
                break
        deq.append(i)

    for i in range(k, len(nums)):
        result.append(nums[deq[0]])

        if deq[0] < i-k+1:
            deq.popleft()

        while len(deq) > 0:
            if nums[deq[-1]] < nums[i]:
                deq.pop()
            else:
                break
        deq.append(i)
    result.append(nums[deq[0]])

    return result

nums = [1,2,1]
k = 2
print maxSlidingWindow(nums, k)