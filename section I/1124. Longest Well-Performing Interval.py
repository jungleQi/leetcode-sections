def longestWPI(hours):
    score = res = 0
    seen = {}

    for i,hour in enumerate(hours):
        score = score + 1 if hour>8 else score-1

        if score > 0:
            res = i+1
            continue

        seen.setdefault(score, i)
        if score-1 in seen:
            res = max(res, i-seen[score-1])

    return res

hours = [9,9,9,9,1,1,1,1,1,9]
#hours = [8,10,6,16,5]
print longestWPI(hours)