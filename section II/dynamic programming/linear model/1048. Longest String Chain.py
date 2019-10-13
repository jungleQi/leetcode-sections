def longestStrChain(words):
    bucket = [dict() for _ in range(16)]

    for i, w in enumerate(words): bucket[len(w) - 1][w] = i

    dp = [1] * len(words)

    for i, buck in enumerate(bucket):

        if i == 0 or len(bucket) == 0 or len(bucket[i - 1]) == 0:
            continue

        prev = bucket[i - 1]

        for word in buck:
            idx = buck[word]

            for i in range(len(word)):
                sub = word[:i] + word[i + 1:]
                if sub in prev:
                    dp[idx] = max(dp[idx], dp[prev[sub]] + 1)

    return max(dp)

words = ["a"]
print(longestStrChain(words))
