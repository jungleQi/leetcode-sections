#-*-coding:utf-8-*-
import collections
import sys
import copy
import time

def preorder_print(root):
    if not root:
        return

    print(root.val)
    preorder_print(root.left)
    preorder_print(root.right)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

A = [1,3,5,7]

class Row(int):
    def __getitem__(self, j):
        return float(self) / A[~j], [int(self), A[~j]]

def _conver2Timestamp(timestr):
    timestr = timestr.strip()
    # 转换成时间数组
    timeArray = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    return timestamp

def convert2Timestamp(timelogFile, stampLogFile):
    timefile = open(timelogFile, "r")
    times = timefile.readlines()

    cnt = len(times)
    i = 1
    intervs = []
    while i < cnt:
        lastTime = _conver2Timestamp(times[i]) - _conver2Timestamp(times[i-1])
        print(lastTime)
        intervs.append(lastTime)
        i += 1

    timeStr = ",".join([ str(interv//60) for interv in intervs])
    stampFile = open(stampLogFile, "w+")
    stampFile.write(timeStr)
    stampFile.close()

    return

timeFile = "/Users/jungle/Documents/datasets/paral1.txt"
targFile = "/Users/jungle/Documents/datasets/paral1_interv.txt"
convert2Timestamp(timeFile, targFile)