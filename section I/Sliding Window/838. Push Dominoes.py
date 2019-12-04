def pushDominoes(dominoes):
    d = 'L'+dominoes+'R'
    i = 0
    ret = []
    for j in range(1, len(d)):
        if d[j] == '.':continue
        if i: ret += d[i],

        dotcnt = j-i-1
        if d[j] == d[i]:
            ret += d[i]*dotcnt,
        elif d[j] == 'R':
            ret += '.'*dotcnt,
        else:
            ret += 'R'*(dotcnt/2) + '.'*(dotcnt%2) + 'L'*(dotcnt/2),
        i = j

    return "".join(ret)

#Input: ".L.R...LR..L.."
#Output: "LL.RR.LLRRLL.."
dominoes = "R..L..RR...LLLR"
# "R..L"
print(pushDominoes(dominoes))


