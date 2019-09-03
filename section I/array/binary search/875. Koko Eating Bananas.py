import math

def minEatingSpeed(piles, H):
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo+hi)/2
        hours = sum((p-1)/mid+1 for p in piles)

        if hours > H:
            lo = mid+1
        else:
            hi = mid

    return hi

piles = [30,11,23,4,20]
H = 6
print minEatingSpeed(piles, H)