def validateStackSequences(pushed, popped):
    i, j, N, M = 0, 0, len(popped), len(pushed)
    stack = []
    while i<N:
        while j<M and (not stack or stack[-1] != popped[i]):
            stack += pushed[j],
            j += 1

        if stack[-1] == popped[i]:
            stack.pop()
            i += 1
        elif j == M and stack:
            return False

    return True

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print validateStackSequences(pushed, popped)