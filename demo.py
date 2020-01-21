def expand(S):
    n = len(S)
    ret = []

    def _helper(pos, path):
        if pos == n:
            ret.append(path)
            return

        if S[pos] == '{':
            end = pos
            while S[end] != '}': end += 1
            opts = S[pos:end].split(",")
            for c in opts:
                _helper(end+1, path+c)
        else:
            _helper(pos+1,path+S[pos])

    _helper(0, "")
    return ret

S = "{a,b}def"
print(expand(S))






