def findClosestElements(arr, k, x):
    cnt = len(arr)
    left, right = 0, cnt-1
    mid = -1
    while left < right:
        mid = (left+right)//2
        if arr[mid] == x:
            break
        elif arr[mid] < x:
            left = mid+1
        else:
            right = mid

    if mid>=0 and arr[mid] == x:
        right = mid
    elif right >= 1 and arr[right]-x > x-arr[right-1]:
        right -= 1

    left = right
    k -= 1
    while k > 0:
        if left > 0:
            if right < cnt-1:
                if x-arr[left-1] <= arr[right+1]-x:
                    left -= 1
                else:
                    right += 1
            else:
                left -= k
                break
        else:
            right += k
            break
        k -= 1

    return arr[left:right+1]

arr = [1]
k = 1
x = 1
ret = findClosestElements(arr, k, x)
print(ret)