def wordBreak(s, wordDict):
    N = len(s)
    dp = [True]+[False]*N

    for i in range(N + 1):
        for word in wordDict:
            l = len(word)

            if l<=i :
                dp[i] = dp[i] or (dp[i-l] and word == s[i-l:i])

    return dp[-1]

s = "applepenapple"
wordDict = ["apple", "pen"]
#s = "catsandog"
#wordDict = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s, wordDict))