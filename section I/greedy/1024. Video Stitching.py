

def videoStitching(clips, T):
    #c[0]<=prevleft 获取curleft最大值
        #扩展cufleft
    #c[0] > prevleft:
        #切换prevleft, curleft
        #证明扩展的curleft起效纳入，cnt+=1

    # 判断是否达到T
    clips.sort(key=lambda x:x[0])
    prevleft, curleft,cnt = 0,0,0
    isFirst = True
    for clip in clips:
        if clip[0]<=prevleft:
            if clip[1] > prevleft and isFirst:
                cnt += 1
                isFirst = False
            curleft = max(clip[1], curleft)
        else:
            if clip[0]<=curleft:
                prevleft, curleft = curleft, clip[1]
                if clip[1] > prevleft:
                    cnt += 1
                    isFirst = False
                else:
                    isFirst = True
            else:
                return -1
        if curleft >= T: break
    return cnt if curleft >= T else -1

def online_videoStitching(clips, T):
    prev_max_end, cur_max_end, cnt = -1,0,0
    for start, end in sorted(clips):
        if start > cur_max_end or cur_max_end >= T:
            break
        if prev_max_end < start <= cur_max_end:
            prev_max_end , cnt = cur_max_end, cnt+1
        cur_max_end = max(cur_max_end, end)
    return cnt if cur_max_end >= T else -1

#clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
clips = [[0,4]]
print(online_videoStitching(clips, 6))