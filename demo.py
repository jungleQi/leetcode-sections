#coding=utf-8
import sys

def _get_intersection(wavnames, txtnames):
    wavnames.sort()
    txtnames.sort()

    intersection = []
    M, N = len(wavnames), len(txtnames)
    i, j = 0, 0
    while i<M and j < N:
        if wavnames[i] == txtnames[j]:
            intersection += wavnames[i],
            i += 1
            j += 1
        elif wavnames[i] > txtnames[j]: j += 1
        else: i += 1

    return intersection

wavnames = ["abcd", "accd", "4sa","abdd", "abe1","ee"]
txtnames = ["1a", "abcc", "a", "accd", "a1","abdd","abed","ea"]
print(_get_intersection(wavnames, txtnames))