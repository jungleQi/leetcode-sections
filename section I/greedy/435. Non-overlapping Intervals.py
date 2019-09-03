def eraseOverlapIntervals(intervals):
    if not intervals: return 0
    sort_intevs = sorted(intervals, key=lambda x:x[1])
    curCnt, totalCnt = 0, len(sort_intevs)
    prevRear = sort_intevs[0][0]
    for interv in sort_intevs:
        if prevRear <= interv[0]:
            curCnt += 1
            prevRear = interv[1]

    return totalCnt-curCnt

intervals = [[1,2],[2,3]]
print eraseOverlapIntervals(intervals)