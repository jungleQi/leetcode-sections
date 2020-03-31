#coding=utf-8

from utils import *
import collections

def findItinerary(tickets):
    arrivals = collections.defaultdict(list)
    for ticket in tickets:
        arrivals[ticket[0]].append(ticket[1])

    visitor = collections.defaultdict(list)
    for key in arrivals.keys():
        visitor[key] = [False]*len(arrivals[key])

    def travel(dept, path, n, ans):
        if n == N:
            ans.append(path)
            return True
        if not arrivals[dept] and n<N:
            return False

        for i, arrival in enumerate(arrivals[dept]):
            if not visitor[dept][i]:
                visitor[dept][i] = True
                ret = travel(arrival, path+[arrival], n+1, ans)
                visitor[dept][i] = False

                if ret: return True
        return False

    N = len(tickets) + 1
    ans = []
    travel("JFK", ["JFK"], 1, ans)
    return ans[0]

tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
print(findItinerary(tickets))