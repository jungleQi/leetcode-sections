#coding=utf-8

'''
Given an 7-array equations of strings that represent relationships between variables,
each 6-string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".
Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
'''

#坑：最开始可能陷入逻辑上的陷阱，依照题目的意思把所有的等式和不等式都建立graph,用0/1来区别两种边
#   很艰难的推断后，认为DFS，如果出现出一个环，这个环内的不等边(1)只有1个，就认为出现了矛盾
#   这种逻辑本身很复杂，testcase有一条否定了这种方案，不知道是代码有bug，还是判别方式本身有漏洞

#比较自然的思维方式：对所有==的建立一个graph，依次拿每个src!=dst去graph找路径[src ... dst]，如果存在
#这样的路径，那就认为出现了矛盾，立即返回就行

#The idea here is to build a direct 3-graph comprising of nodes connected by '=='.
#Subsequently, traverse the direct 3-graph to check whether you have a "reachable"
#  path between nodes connected by '!=' in the original direct 3-graph.
#If one such path exists, then the equation is not feasible.

import collections
def equationsPossible(equations):
    def dfs(prev, src, dst, visitor):
        if src == dst: return True
        for nei in graph[src]:
            if nei == prev or nei in visitor:
                continue
            if dfs(src, nei, dst, visitor+[nei]):
                return True

        return False

    graph = collections.defaultdict(list)
    pairs = collections.defaultdict(list)
    for item in equations:
        if item[1] == '!':
            pairs[item[0]].append(item[3])
        else:
            graph[item[0]].append(item[3])
            graph[item[3]].append(item[0])

    for src, dsts in pairs.items():
        print(src, dsts)
        for dst in dsts:
            ans = dfs("", src, dst, [src])
            if ans: return False
    return True


equations = ["k==s","b==c","s==l","j==o","r!=i","e!=c","h!=d","p!=j","f==h","g==p","i!=k","l!=i","g!=r","h!=a","j!=s","a!=x","u==f","y!=p","a!=p","r!=p","m!=s","j!=n","a!=s","f==w","g!=l","l!=n","s!=m","b!=h","k==v","y!=u","a!=h","p!=b","f!=y","r==q","s!=u","f!=s","l!=n","i==t","n!=v","l!=y","x!=e","e!=j","v!=d","c!=y","e!=j","f!=v","o!=k","o!=q","k!=p","r!=u","u!=l","i!=w","j!=q","x!=q","h!=o","k!=f","p!=a","j!=u","a!=i","a==a","l!=n","q!=w","x!=e","o!=s","x!=h","j==j","t!=k","o!=k","w!=g","i!=u","d!=o","l!=o","b!=n","n!=a","y!=w","o!=h","f!=m","n!=b","x!=h","e!=v","t!=j","r!=a","b!=y","p!=q","o!=x","y!=a","b!=o","a!=o","h!=a","x!=t","l!=h","b!=x","s!=p","j!=k","b!=s","p!=d","r!=m","f!=a","u!=r","f==r"]
print(equationsPossible(equations))