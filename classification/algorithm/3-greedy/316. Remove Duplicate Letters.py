'''
1081. Smallest Subsequence of Distinct Characters

Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.

Example 1:
Input: "cdadabcc"
Output: "adbc"
'''

def smallestSubsequence(text):
    stack = []
    for i, c in enumerate(text):
        if c in stack: continue
        while stack and c < stack[-1] and stack[-1] in text[i:]:
            stack.pop()

        stack += c,
    return "".join(stack)


'''
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:
Input: "bcabc"
Output: "abc"

Example 2:
Input: "cbacdcbc"
Output: "acdb"
'''

# Greedy - Solving with Stack
def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    for i, c in enumerate(s):
        if c in stack: continue
        while stack and c < stack[-1] and stack[-1] in s[i:]:
            stack.pop()

        stack += c,
    return "".join(stack)