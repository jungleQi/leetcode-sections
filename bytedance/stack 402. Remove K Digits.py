def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    stack = []
    for i, n in enumerate(num):
        while stack and k > 0:
            if stack[-1] <= n: break
            stack.pop()
            k -= 1

        #case: "10200" 2
        if not stack and n == '0': continue

        stack.append(n)

    #
    ans = stack[:-k] if k > 0 else stack
    return "".join(ans) if ans else "0"