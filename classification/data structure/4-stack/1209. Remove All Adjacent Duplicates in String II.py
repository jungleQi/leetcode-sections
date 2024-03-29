'''
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them,
causing the left and the right side of the deleted substring to concatenate together.

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
    stack = [['#', 0]]
    for c in s:
        if stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c, 1])
    return ''.join(c * k for c, k in stack)

s = "aa"
k = 2
print(removeDuplicates(s, k))

