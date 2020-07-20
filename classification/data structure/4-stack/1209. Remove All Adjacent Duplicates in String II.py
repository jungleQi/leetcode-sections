'''
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made.
It is guaranteed that the answer is unique.

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
'''

def removeDuplicates(s, k):
    stack = []
    for i, c in enumerate(s):
        if stack and stack[-1][1] == k-1 and stack[-1][0] == c:
            stack.pop()
        else:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c,1])
    ans = ""
    while stack:
        top = stack.pop()
        ans = top[0]*top[1]+ans
    return ans

s = "aa"
k = 2
print(removeDuplicates(s, k))

