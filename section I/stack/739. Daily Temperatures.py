def dailyTemperatures(T):
    res = [0]*len(T)
    stack = []
    for i in range(len(T)-1, -1, -1):
        while stack and T[stack[-1]] <= T[i]:
            stack.pop()

        if stack:
            res[i] = stack[-1]-i
        stack += i,

    return res


T = []
print dailyTemperatures(T)