def candy(ratings):
    children = {}
    for idx, rating in enumerate(ratings):
        if rating not in children:
            children[rating] = [idx]
        else:
            children[rating].append(idx)
    sortChildren = sorted(children.items(), key=lambda x:x[0])

    N = len(ratings)
    candies = [1]*N
    for item in sortChildren:
        curRating = item[0]
        idxs = item[1]
        for i in idxs:
            li, ri = i-1, i+1
            if li < 0: li = 0
            if ri >= N: ri = N - 1
            if curRating <= ratings[li] and curRating <= ratings[ri]:
                continue

            if curRating > ratings[li]:
                candies[i] = max(candies[li]+1, candies[i])
            if curRating > ratings[ri]:
                candies[i] = max(candies[ri]+1, candies[i])

    return sum(candies)


ratings = [1,0,2]
print candy(ratings)
