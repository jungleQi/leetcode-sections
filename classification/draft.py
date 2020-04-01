#coding=utf-8

import collections
def canVisitAllRooms(rooms):
    N = len(rooms)
    visitor = [False]*N

    def dfs(curRoom):
        visitor[curRoom] = True
        for nextRoom in rooms[curRoom]:
            if nextRoom == curRoom or visitor[nextRoom]:
                continue
            dfs(nextRoom)

    dfs(0)
    return all(visitor)

rooms = [[1,3],[3,0,1],[2],[0]]
print(canVisitAllRooms(rooms))