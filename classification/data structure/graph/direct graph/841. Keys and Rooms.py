#coding=utf-8

'''
There are N rooms and you start in room 0.
Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i],
and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.
A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).
You can walk back and forth between rooms freely.
Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
'''

# 从指定的0出发，对graph进行遍历
# 进入哪个房间获得钥匙再继续去开门，其实就是单向的遍历而不需要回溯，用BFS正合适
# 进入过的房间计入visitor，一方面是结果，另一方面避免回溯，一直向前

import collections
def canVisitAllRooms_BFS(rooms):
    deque = collections.deque([0])
    visitor = set()

    while deque:
        i = deque.popleft()
        if i in visitor: continue
        visitor.add(i)
        for nextRoom in rooms[i]:
            if nextRoom in visitor: continue
            deque.append(nextRoom)

    return len(visitor) == len(rooms)

def canVisitAllRooms_DFS(rooms):
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

rooms = [[1],[1]]
print(canVisitAllRooms_BFS(rooms))