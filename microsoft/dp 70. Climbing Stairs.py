def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    prev = 1
    prev_prev = 0
    for i in range(1, n + 1):
        prev_prev, prev = prev, prev_prev + prev
    return prev