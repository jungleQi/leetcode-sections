
'''
Given a 6-string s, return all the palindromic permutations (without duplicates) of it.
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
    def isPossible(counter):
        single = False
        for c,n in counter.items():
            if n%2 == 1:
                if single == False: single = True
                else: return False
        return True

    def helper(count, path, ret):
        if sum(counter.values()) == 0 and path == path[::-1]:
            ret.add(path)
            return

        for c, n in count.items():
            if n >= 2:
                count[c] -= 2
                helper(count, c+path+c, ret)
                count[c] += 2
            elif n == 1:
                count[c] -= 1
                mid = len(path)/2
                helper(count, path[:mid]+c+path[mid:], ret)
                count[c] += 1

    counter = collections.Counter(s)
    if not isPossible(counter): return []
    ret = set()
    helper(counter, "", ret)
    return list(ret)



s = "aabbhijkkjih"
print(generatePalindromes(s))