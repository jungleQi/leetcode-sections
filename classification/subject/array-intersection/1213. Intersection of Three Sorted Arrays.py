'''
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order,
return a sorted array of only the integers that appeared in all three arrays.

Example 1:
Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
'''

def arraysIntersection(arr1, arr2, arr3):
    L,M,N = len(arr1), len(arr2), len(arr3)
    i,j,k = 0,0,0
    ans = []
    while i<L and j<M and k<N:
        if arr1[i] == arr2[j] and arr1[i] == arr3[k]:
            ans.append(arr1[i])
            i += 1
            j += 1
            k += 1
            continue
        curmax = max(arr1[i], arr2[j], arr3[k])
        if arr1[i] < curmax: i += 1
        if arr2[j] < curmax: j += 1
        if arr3[k] < curmax: k += 1

    return ans

#该方法可以推广到K个
def arraysIntersection_K(arr1, arr2, arr3):
    def twoArraysIntersection(a,b):
        i1,i2 = 0,0
        M,N = len(a),len(b)
        ans = []
        while i1<M and i2<N:
            if a[i1] == b[i2]:
                ans.append(a[i1])
                i1 += 1
                i2 += 1
            elif a[i1] < b[i2]:
                i1 += 1
            else:
                i2 += 1
        return ans

    arr = twoArraysIntersection(arr1,arr2)
    return twoArraysIntersection(arr,arr3)


arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
print(arraysIntersection_K(arr1, arr2, arr3))