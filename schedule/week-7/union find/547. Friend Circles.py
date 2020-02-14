#coding=utf-8

'''
There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature.
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2

Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
'''

import collections
def findCircleNum(M):
    N = len(M)
    visitor = set()

    dt = collections.defaultdict(list)
    for i in range(N):
        for j in range(i+1,N):
            if M[i][j] == 1:
                dt[i].append(j)
                dt[j].append(i)

    def dfs(m, path, ret):
        if m in visitor:
            ret.append(m)
            return

        for n in dt[m]:
            if n in path: continue
            path.add(n)
            dfs(n, path, ret)

    circles = 0
    for i in range(N):
        out = []
        st = {i}

        dfs(i, st, out)
        visitor = visitor.union(st)
        if not out:
            circles += 1

    return circles if circles > 0 else 1


# M = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
#      [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
#      [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
#      [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
#      [0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],
#      [0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
#      [0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],
#      [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
#      [0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
#      [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
#      [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],
#      [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
#      [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
#      [0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
#      [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]

M = [[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
     [0,1,0,0,0,1,0,0,0,0,0,0,0,0,0],
     [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
     [0,1,0,0,0,1,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,1,0,0,0,0,1,0,0,0],
     [0,0,0,0,0,0,0,1,0,0,0,1,1,0,0],
     [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
     [0,0,0,0,0,0,1,1,0,0,1,1,0,0,1],
     [0,0,0,0,1,1,0,1,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1]]
print(findCircleNum(M))