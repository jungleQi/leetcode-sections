'''
An encoded string s is given.
To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d more times in total.
Now for some encoded string s, and an index k, find and return the k-th letter (1 indexed) in the decoded string.

Example 1:
Input: s = "leet2code3", k = 10
Output: "o"
Explanation:
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
'''

def decodeAtIndex_TLE(s, k):
    cur = ""
    for c in s:
        #字符串的实际拼接，比较低效
        if c.isdigit():
            cur = cur*int(c)
        else:
            cur += c
        if len(cur) > k:
            break
    return cur[k-1]

def decodeAtIndex(S, K):
    curlen = 0
    for c in S:
        if c.isdigit():
            curlen = int(c) * curlen
        else:
            curlen += 1

    for c in reversed(S):
        K = K % curlen
        if K == 0 and c.isalpha():
            return c

        if c.isdigit():
            curlen = curlen / int(c)
        else:
            curlen -= 1

s = "y959q969u3hb22odq595"
k = 222280369
print(decodeAtIndex(s, k))