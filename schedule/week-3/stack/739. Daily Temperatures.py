#coding=utf-8

'''
Given a list of daily temperatures T, return a list such that, for each day in the input,
 tells you how many days you would have to wait until a warmer temperature.
 If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
'''

#正序遍历只能通过常规的方式处理，比较低效
#逆序遍历能很好的利用stack，高效的处理

def dailyTemperatures(T):
    N = len(T)
    ret = [0]*N
    stack = []

    for i in range(N-1, -1, -1):
        while stack and T[stack[-1]]<=T[i]:
            stack.pop()
        if stack:
            ret[i] = stack[-1]-i
        stack.append(i)
    return ret

T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(T))