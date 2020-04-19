#coding=utf-8
from utils import Node
import heapq
import collections

def lastStoneWeightII(stones):
    stoneSum = sum(stones)

    dp = {0}
    for weight in stones:
        dp |= {weight+i for i in dp}

    return min([abs(stoneSum-i-i) for i in dp])