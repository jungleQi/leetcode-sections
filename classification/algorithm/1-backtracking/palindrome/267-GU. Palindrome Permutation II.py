
'''
Given a string s, return all the palindromic permutations (without duplicates) of it.
Return an empty list if no palindromic permutation could be form.

Example 1:
Input: "aabb"
Output: ["abba", "baab"]

Example 2:
Input: "abc"
Output: []
'''

#Time complexity : O((n/2+1)!)

import collections
def generatePalindromes(s):
    def helper(counter, cur, ret):
        if (sum(counter.values()) == 0):
            ret.append(cur)
            return

        for key, val in counter.items():
            if val % 2 != 0: return
            if val == 0: continue

            counter[key] -= 2
            helper(counter, key + cur + key, ret)
            counter[key] += 2

    counter = collections.Counter(s)
    ret = []
    cur = ""
    for key, val in counter.items():
        if val % 2 != 0:
            cur += key
            counter[key] -= 1
    if len(cur) > 1: return ret

    helper(counter, cur, ret)
    return ret



s = "aabbhijkkjih"
print(generatePalindromes(s))