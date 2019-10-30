def findLongestChain_dp(pairs):
    pairs.sort(key=lambda x:(x[0],x[1]))

    N, maxlen = len(pairs), 1
    dp = [1]*N
    for i in range(1,N):
        if pairs[i][0] == pairs[i - 1]:
            dp[i] = dp[i - 1]
        else:
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)

        maxlen = max(dp[i], maxlen)

    return maxlen

def findLongestChain_greedy(pairs):
    import operator
    cur, ans = float('-inf'), 0
    for x, y in sorted(pairs, key=operator.itemgetter(1)):
        if cur < x:
            cur = y
            ans += 1
    return ans

pairs = [[1,2], [2,3], [3,6],[4,5]]
print(findLongestChain_greedy(pairs))