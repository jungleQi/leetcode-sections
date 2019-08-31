def letterCasePermutation(S):
    cnt = len(S)
    solutions = []

    def travel(idx,res):
        if idx == cnt:
            solutions.append(res)
            return

        if S[idx].islower():
            travel(idx+1, res+S[idx].upper())
        elif S[idx].isupper():
            travel(idx+1, res+S[idx].lower())

        travel(idx + 1, res + S[idx])

    travel(0, "")
    return solutions

print(letterCasePermutation(""))