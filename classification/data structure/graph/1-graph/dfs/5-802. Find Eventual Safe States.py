#coding=utf-8

'''
In a directed direct graph, we start at some node and every turn, walk along a directed edge of the direct graph.
If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.
 More specifically, there exists a natural number K so that for any choice of where to walk,
 we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed direct graph has N nodes with labels 0, 1, ..., N-1, where N is the length of direct graph.
The direct graph is given in the following form: direct graph[i] is a list of labels j such that (i, j) is a directed edge of the direct graph.

Example:
Input: direct graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above direct graph.
'''

#WHITE  表示没有被访问过
#GRAY   表示已经被访问，正在访问其相邻节点
#BLACK  表示该节点所有的相邻节点都已经深度优先访问结束

#visit node，entry的时候mark为GRAY, exit的时候mark为BLACK。
# 如果我们在DFS过程中看到了GRAY，它肯定是一个cycle

#厘清：
# 1.回溯点或者分支点，是在recursion调用产生，它的调用返回，也是一个分支遍历结束后的状态
# 2.pruning有两处：
#   2.1 递归函数入口处：如果已经被定性过GRAY or BLACK，就返回
#   2.2 产生分支处：对neighbor的判断，如果neighbor已经被定性为BLACK就无需再对该neighbor分支进行判断；
#       如果neighbors中，只要出现了一个neighbor是GRAY，或者neighbor的分支返回False，整个递归链条就层层返回，全是GRAY

#回顾：有很多graph问题

import collections
def eventualSafeNodes(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = collections.defaultdict(int)

    def dfs(i):
        if color[i] != WHITE:#被访问过
            # 如果被前序访问过，后续又访问，说明有环；如果该点已经遍历结束,那前序加上该点也能遍历到尽头
            return color[i] == BLACK

        #entry设置为GRAY
        color[i] = GRAY
        for neigh in graph[i]:
            #如果领域节点已经顺利遍历完毕，就不用再判断
            if color[neigh] == BLACK:
                continue
            #如果领域节点被前序已经访问过，或者对领域节点进行dfs判断有环，就返回失败
            if color[neigh] == GRAY or not dfs(neigh):
                return False

        #exit设置为成功访问结束
        color[i] = BLACK
        return True

    #过滤判断第i个是否满足，如果判断为真，就列入返回列表
    return filter(dfs, range(len(graph)))

graph = [[1,2],[2],[5],[0],[5],[],[]]
print(eventualSafeNodes(graph))
