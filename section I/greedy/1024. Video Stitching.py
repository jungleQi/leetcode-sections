def videoStitching(clips, T):
    clips.sort(key=lambda x:(x[0],x[1]))
    if clips[0][0] > 0: return -1

    res, curMaxEnd, lastEndNum = 1, 0, 0
    for area in clips:
        if area[0]<=lastEndNum:
            curMaxEnd = max(curMaxEnd, area[1])
        else:
            res += 1
            lastEndNum = curMaxEnd
            curMaxEnd = area[1]

        if area[1] >= T and area[0] <= lastEndNum:
            return res

    return -1

clips = [[8,10],[17,39],[18,19],[8,16],[13,35],[33,39],[11,19],[18,35]]
T = 20
#clips = [[0,2],[4,8]]
#T = 5
print(videoStitching(clips, T))