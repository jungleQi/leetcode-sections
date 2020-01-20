def generateAbbreviations_iterator(word):
    n = len(word)
    ret = []

    def _helper(pos, cur, count):
        if pos == n:
            ret.append(cur+str(count) if count>0 else cur)
            return

        _helper(pos+1, cur, count+1)
        _helper(pos+1, cur+(str(count) if count>0 else "")+word[pos], 0)

    _helper(0, "", 0)
    return ret

print(generateAbbreviations_iterator("word"))