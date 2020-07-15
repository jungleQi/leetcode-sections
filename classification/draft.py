# T = [73, 74, 75, 71, 69, 72, 76, 73]
def dailyTemperatures(T):
    N = len(T)
    stack = []
    ans = [0]*N
    for i,n in enumerate(T):
        while stack and T[stack[-1]]<n:
            idx = stack.pop()
            ans[idx] = i-idx
        stack.append(i)
    return ans

T = []
print(dailyTemperatures(T))

