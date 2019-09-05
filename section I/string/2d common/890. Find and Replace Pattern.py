def findAndReplacePattern(words, pattern):
    def match(word):
        wdict, pdict = {}, {}
        for w,p in zip(word, pattern):
            if w not in wdict: wdict[w] = p
            if p not in pdict: pdict[p] = w

            if (wdict[w], pdict[p]) != (p, w):
                return False
        return True

    return filter(match, words)

words = ["acc"]
pattern = "abb"
print findAndReplacePattern(words, pattern)