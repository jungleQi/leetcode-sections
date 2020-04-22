#coding=utf-8
from utils import Node
import heapq
import collections

def numTrees(n):
    G = [0]*(n+1)
    G[0] = 1
    for i in range(1, n+1):
        for j in range(1,i+1):
            G[i] += G[j-1]*G[i-j]
    return G[-1]

print numTrees(3)