# coding=utf-8
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

#
# 能回到1号点返回 Yes，否则返回 No
# @param param int整型一维数组 param[0] 为 n，param[1] 为 m
# @param edge Point类一维数组 Point.x , Point.y 分别为一条边的两个点
# @return string字符串
#
#
import collections


def solve(edge):
    def travel(node, visitor, parent, target):
        for nei in graph[node]:
            if nei in visitor or nei == parent: continue
            if nei == target: return True

            if travel(nei, visitor + [nei], node, target):
                return True
        return False

    graph = collections.defaultdict(list)
    for item in edge:
        graph[item[0]].append(item[1])
        graph[item[1]].append(item[0])

    target = 1
    ret = travel(1, [], -1, target)
    return "Yes" if ret else "No"

edge = [(1, 2), (2, 3), (3, 4), (4, 1)]
print solve(edge)