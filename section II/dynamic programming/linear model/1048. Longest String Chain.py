def longestStrChain(words):
    wordsmap = {}
    for word in words:
        wordlen = len(word)
        if wordlen not in wordsmap:
            wordsmap[wordlen] = [word]
        else:
            wordsmap[wordlen] += word,

    sortWords = sorted(wordsmap.items(), key=lambda x:x[0], reverse=True)

    length = {}
    maxLen = 1
    for idx, item in enumerate(sortWords):
        wlen, words = item[0], item[1]

        for curword in words:
            length[curword] = 1

        if idx == 0: continue

        for curword in sortWords[idx-1][1]:
            curIdx = len(curword)-1
            while curIdx>=0:
                delWord = curword[:curIdx]+curword[curIdx+1:]
                if delWord in words:
                    length[delWord] = max(length[delWord], length[curword]+1)
                    maxLen = max(maxLen, length[delWord])

                curIdx -= 1

    return maxLen

words = ["a"]
print(longestStrChain(words))
