def shiftingLetters(S, shifts):
    for i in range(len(shifts)-2, -1, -1):
        shifts[i] += shifts[i+1]

    res = ""
    for i,c in enumerate(S):
        offset = shifts[i]%(ord('z')-ord('a')+1)
        if (ord(c)+offset) <= ord('z'):
            res += chr(ord(c)+offset)
        else:
            res += chr(ord('a')+ord(c)+offset-ord('z')-1)

    return res

S = "a"
shifts = [3]
print shiftingLetters(S, shifts)