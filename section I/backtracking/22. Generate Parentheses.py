def generateParenthesis(n):
    solutions = []
    def travel(n, m,res):
        if n==0 and m == 0:
            solutions.append(res)
            return

        if n > m or n<0 or m<0:
            return

        travel(n-1, m, res+'(')
        travel(n, m-1, res + ')')

    travel(n, n, "")
    return solutions

print generateParenthesis(3)
