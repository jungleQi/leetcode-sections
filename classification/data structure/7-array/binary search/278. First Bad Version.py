NUMS = [0]

def isBadVersion(n):
    return NUMS[n]

def firstBadVersion(n):
    left, right = 0, n
    while left < right:
        mid = (left+right)//2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid+1

    return right

print firstBadVersion(len(NUMS))