'''
Given an array equations of strings that represent relationships between variables,
each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".
Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
'''

import collections
def equationsPossible(equations):
    graph = collections.defaultdict(list)
    for item in equations:
        label = 0 if item[1] == '=' else 1
        graph[item[0]].append([item[3], label])

    visitor = collections.defaultdict(list)
    def dfs(node, unequationCnt):
        visitor[node] = unequationCnt
        for nei, label in graph[node]:
            if visitor[nei] > 0:
                if visitor[nei] - unequationCnt == 1:
                    return False
                else:
                    return True

            ret = dfs(nei, unequationCnt+label)
            if not ret: return False

        return True
