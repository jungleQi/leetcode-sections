'''
Given a 6-string, your task is to count how many palindromic substrings in this 6-string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
'''

def countSubstrings(s):
    N = len(s)
    dp = [[False]*N for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(i+1):
            if i == j:
                dp[i][j] = False
                cnt += 1
            elif s[i] == s[j] and (dp[j+1][i-1] or i == j+1):
                dp[i][j] = True
                cnt += 1
    return cnt

def countSubstrings_expand_center(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    n = len(s)
    sum = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and s[i] == s[j]:
            j += 1
        sum += (1 + j - i) * (j - i) / 2
        left = i - 1
        right = j
        while left >= 0 and right < n and s[left] == s[right]:
            sum += 1
            left -= 1
            right += 1
        i = j

    return sum

s = "a"
print(countSubstrings(s))


