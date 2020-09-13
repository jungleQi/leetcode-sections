def findMinArrowShots(points):
    if not points: return 0
    sort_pts = sorted(points, key=lambda x:x[1])
    prevRear = sort_pts[0][0]-1

    arrow = 0
    for pt in sort_pts:
        if pt[0] > prevRear:
            prevRear = pt[1]
            arrow += 1

    return arrow

points = [[2,8],[8,9]]
print findMinArrowShots(points)