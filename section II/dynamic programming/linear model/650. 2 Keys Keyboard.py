'''
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

1.Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
2.Paste: You can paste the characters which are copied last time.


Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted.
Output the minimum number of steps to get n 'A'.
'''

import sys
def minSteps(n):
    dp = [i for i in range(n+1)]

    for i in range(2, n + 1):
        for j in range(2, i / 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i / j)

    return dp[-1]

print(minSteps(2))
