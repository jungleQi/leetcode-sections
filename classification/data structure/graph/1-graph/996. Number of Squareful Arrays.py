#coding=utf-8

'''
Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements,
their sum is a perfect square.

Return the number of permutations of A that are squareful.
Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

Example 1:

Input: [1,17,8]
Output: 2
Explanation:
[1,8,17] and [17,8,1] are the valid permutations.
'''

import collections
def numSquarefulPerms_noGrace(A):
    graph = collections.defaultdict(list)
    count = collections.Counter(A)
    for x in count:
        for y in count:
            if int((x + y) ** .5 + 0.5) ** 2 == x + y:
                graph[x].append(y)

    N = len(A)
    def dfs(i, path, ret):
        count[i] -= 1 #相比 在line 35前后加上计数的增减，计数放在这里的好处，是不用再外面line 40前后也加这样一对
        if len(path) == N:
            ret[0] += 1
        else:
            for child in graph[i]:
                if count[child] == 0: continue
                dfs(child, path+[child], ret)
        count[i] += 1

    ret = [0]
    for node,n in count.items():
        dfs(node, [node], ret)
    return ret[0]

#这种固定的总元素个数，全部遍历，最后有多少种可能的code pattern：
#1.可能的话，用counter对每种元素计数，应对初始数组可能有重复元素
#2.为了dfs完毕，透出计数结果，只在if else 之外，做一次返回ans。if 内结束该次遍历 返回1；esle内ans置0，将递归返回的值，累加到ans
#3.遍历过程中，入栈时数目减1 出栈时数目加1，在dfs函数体内进行.
#4.对多个元素的计算，汇总成一个结果返回，为了简洁，可以考虑用sum() 或者 filter() ,返回总数或者列表

def numSquarefulPerms_Grace(A):
    graph = collections.defaultdict(list)
    count = collections.Counter(A)
    for x in count:
        for y in count:
            if int((x + y) ** .5 + 0.5) ** 2 == x + y:
                graph[x].append(y)

    def dfs(x, todo):
        count[x] -= 1
        if todo == 0:
            ans = 1
        else:
            ans = 0
            for y in graph[x]:
                if count[y]:
                    ans += dfs(y, todo-1)
        count[x] += 1
        return ans

    return sum(dfs(i, len(A)-1) for i in graph)

A = [1,8,17]
print(numSquarefulPerms_Grace(A))