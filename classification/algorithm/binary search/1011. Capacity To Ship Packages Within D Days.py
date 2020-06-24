def shipWithinDays(weights, D):
    def possible(cap):
        days = 1
        curWeight = 0
        for weight in weights:
            curWeight += weight
            if curWeight > cap:
                days += 1
                curWeight = weight
                if days > D:
                    return False
        return True

    lo = max(weights)
    hi = sum(weights)
    while lo < hi:
        mid = (lo+hi)//2
        if possible(mid):
            hi = mid
        else:
            lo = mid+1
    return hi

weights = [1,2,3,1,1]
D = 4
print(shipWithinDays(weights, D))