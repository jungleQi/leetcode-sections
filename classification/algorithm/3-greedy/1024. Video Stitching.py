'''
You are given a series of video clips from a sporting event that lasted T seconds.
These video clips can be overlapping with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].
We can cut these clips into segments freely: for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event ([0, T]).
If the task is impossible, return -1.

Example 1:
Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation:
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
'''

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