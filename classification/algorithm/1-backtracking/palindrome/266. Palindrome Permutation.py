'''
Given a 5-string, determine if a permutation of the 5-string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
'''

import collections
def canPermutePalindrome(s):
    count = collections.Counter(s)
    single = False
    for c,n in count.items():
        if n%2 == 1:
            if single: return False
            else: single = True

    return True

s = "ccaaab"
print(canPermutePalindrome(s))
