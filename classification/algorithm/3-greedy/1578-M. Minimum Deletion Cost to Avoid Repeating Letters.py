'''
Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words,
after deleting a character, the costs of deleting other characters will not change.

Example 1:
Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
'''


def minCost(s, cost):
    """
    :type s: str
    :type cost: List[int]
    :rtype: int
    """
    remain = 0
    costDel = 0
    for i in range(1, len(s)):
        if s[i] == s[remain]:
            if cost[i] < cost[remain]:
                costDel += cost[i]
            else:
                costDel += cost[remain]
                remain = i
        else:
            remain = i
    return costDel