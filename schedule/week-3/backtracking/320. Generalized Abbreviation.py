#coding=utf-8

'''
Write a function to generate the generalized abbreviations of a word.

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
'''

#类似的combinations问题，一般都能通过backtracking求解
#count: 被省略的字母数量(具有连续性)，pos当前字母在单词中的索引值

def generateAbbreviations(word):
    n = len(word)
    ret = []

    def _helper(pos, cur, count):
        if pos == n:
            ret.append(cur+str(count) if count > 0 else cur)
            return
        _helper(pos+1, cur, count+1)
        _helper(pos+1, cur+(str(count) if count>0 else '')+word[pos], 0)

    _helper(0, "", 0)
    return ret


word = "word"
print(generateAbbreviations(word))
