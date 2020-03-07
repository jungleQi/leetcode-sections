'''
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

1.Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
2.Paste: You can paste the characters which are copied last time.

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted.
Output the minimum number of steps to get n 'A'.

'''

def minSteps(n):
    dp = [i for i in range(n+1)]
    for i in range(3,n+1):
        for j in range(2,i/2+1):
            if i%j == 0:
                dp[i] = min(dp[i], dp[j]+i/j)
                #if i == 741:
                #    print(dp[i],i/j, dp[i/j], i,j)

    return dp[-1]

def minSteps_fast(n):
    if n <= 1: return n
    per_step, acc_step, cur_steps, min_steps = 1, 1, 0, n
    while acc_step <= n:
        if n%acc_step == 0:
            per_step = acc_step
            min_steps = min(min_steps, cur_steps+n/acc_step)
            cur_steps += 1
            acc_step += acc_step
        else:
            acc_step += per_step
        cur_steps += 1

    return min_steps


#25 11 741
print(minSteps_fast(1))