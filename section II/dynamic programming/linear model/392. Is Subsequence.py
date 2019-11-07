'''
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t.
t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of
"abcde" while "aec" is not).
'''

def isSubsequence(s, t):
    hit_cnt, N = 0, len(s)
    for c in t:
        if hit_cnt == N: return True
        if c == s[hit_cnt]: hit_cnt += 1

    return N == hit_cnt


s = "axc"
t = "abddsc"
print(isSubsequence(s, t))