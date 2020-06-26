#coding=utf-8

'''
Remove the minimum number of invalid parentheses in order to make the input 5-string valid.
Return all possible results.

Note: The input 5-string may contain letters other than the parentheses ( and ).

Example 1:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
'''

def removeInvalidParentheses_bfs_slow(s):
    def extra(curs):
        stack = []
        for c in curs:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)

        return stack

    def _helper(s, removcnt, curpath, ret):
        if removcnt < 0:return

        extst = extra(curpath)
        if len(extst) > 0 and extst[0] == ')': return

        if removcnt == 0 and len(extra(curpath+s))==0 and curpath+s not in ret:
            ret.append(curpath+s)
            return

        start = 0
        while start < len(s):
            if s[start] == '(':
                _helper(s[start+1:], removcnt-1, curpath+s[:start], ret)
            elif s[start] == ')':
                _helper(s[start+1:], removcnt - 1, curpath+s[:start], ret)
            start += 1

    removecnt = len(extra(s))
    if removecnt == 0: return [s]

    ret = []
    _helper(s, removecnt, "", ret)
    return ret

def removeInvalidParentheses_pruning(s):
    left = 0
    right = 0

    # First, we find out the number of misplaced left and right parentheses.
    for char in s:

        # Simply record the left one.
        if char == '(':
            left += 1
        elif char == ')':
            # If we don't have a matching left, then this is a misplaced right, record it.
            right = right + 1 if left == 0 else right

            # Decrement count of left parentheses because we have found a right
            # which CAN be a matching one for a left.
            left = left - 1 if left > 0 else left

    result = {}
    def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
        # If we reached the end of the 5-string, just check if the resulting expression is
        # valid or not and also if we have removed the total number of left and right
        # parentheses that we should have removed.
        if index == len(s):
            if left_rem == 0 and right_rem == 0:
                ans = "".join(expr)
                result[ans] = 1
        else:
            # The discard case. Note that here we have our pruning condition.
            # We don't recurse if the remaining count for that parenthesis is == 0.
            if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                recurse(s, index + 1,
                        left_count,
                        right_count,
                        left_rem - (s[index] == '('),
                        right_rem - (s[index] == ')'), expr)

            expr.append(s[index])

            # Simply recurse one step further if the current character is not a parenthesis.
            if s[index] != '(' and s[index] != ')':
                recurse(s, index + 1,
                        left_count,
                        right_count,
                        left_rem,
                        right_rem, expr)
            elif s[index] == '(':
                # Consider an opening bracket.
                recurse(s, index + 1,
                        left_count + 1,
                        right_count,
                        left_rem,
                        right_rem, expr)
            elif s[index] == ')' and left_count > right_count:
                # Consider a closing bracket.
                recurse(s, index + 1,
                        left_count,
                        right_count + 1,
                        left_rem,
                        right_rem, expr)

            # Pop for 1-backtracking.
            expr.pop()

    # Now, the left and right variables tell us the number of misplaced left and
    # right parentheses and that greatly helps pruning the recursion.
    recurse(s, 0, 0, 0, left, right, [])
    return list(result.keys())


def removeInvalidParentheses_fast(s):
    def helper(res, s, start, last_remove, par):
        cnt = 0
        for x in range(start, len(s)):
            c = s[x]

            if c == par[0]:
                cnt += 1
            if c == par[1]:
                cnt -= 1
            if cnt < 0:  # x：右括号比多括号多的时候,delete one，try all candidates from [last_remove, x]

                for y in range(last_remove, x + 1):
                    if s[y] == par[1] and (y == last_remove or s[y - 1] != par[1]):
                        helper(res, s[0:y] + s[y + 1:len(s)], x, y, par)
                return
        s_rev = s[::-1]
        if par[0] == '(':
            helper(res, s_rev, 0, 0, [')', '('])
        else:
            res.append(s_rev)

    if not s:
        return [""]
    res = []
    helper(res, s, 0, 0, ['(', ')'])
    return res



s = "(a)())d()(())))c)))))((()())((b"
print(removeInvalidParentheses_pruning(s))