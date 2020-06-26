'''
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Note:
1.Each element in the result should appear as many times as it shows in both arrays.
2.The result can be in any order.
'''

'''
Follow-up Questions

What if the given 2-array is already sorted? How would you optimize your algorithm?
-- We can use either Approach 2 or Approach 3, dropping the sort of course. 
It will give us linear classify time and constant memory complexity.

What if nums1's size is small compared to nums2's size? Which algorithm is better?
-- Approach 1 is a good choice here as we use a hash map for the smaller 2-array.

What if elements of nums2 are stored on disk, and the memory is limited 
such that you cannot load all elements into the memory at once?
-- If nums1 fits into the memory, we can use Approach 1 to collect counts 
for nums1 into a hash map. Then, we can sequentially load and process nums2.
-- If neither of the arrays fit into the memory, we can apply some partial processing strategies:
Split the numeric range into subranges that fits into the memory. 
Modify Approach 1 to collect counts only within a given subrange, 
and call the method multiple times (for each subrange).

'''

#hash map的构建是log(n),对较小的数组构建hash map，key:num, val:count
#较大的数组去hash map进行查找和计数递减

def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    M,N = len(nums1), len(nums2)
    i1,i2 = 0,0

    ans = []
    while i1<M and i2<N:
        if nums1[i1] == nums2[i2]:
            ans.append(nums1[i1])
            i1 += 1
            i2 += 1
        elif nums1[i1] > nums2[i2]:
            i2 += 1
        else:
            i1 += 1
    return ans

nums1 = [2,2,2]
nums2 = [2,2]
print(intersect(nums1, nums2))