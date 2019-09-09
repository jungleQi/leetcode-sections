def isLongPressedName(name, typed):
    j = 0
    N, M= len(name), len(typed)
    for i in range(N):
        if j>= M: return False

        if name[i] == typed[j]:
            j += 1
        else:
            while j<M and j>0 and typed[j] == typed[j-1]:
                j += 1
            if j==M or typed[j] != name[i]:
                return False
            j += 1
    return True

name = "laiden"
typed = "laiden"
print isLongPressedName(name, typed)