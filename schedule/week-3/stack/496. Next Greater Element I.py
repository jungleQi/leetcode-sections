#coding=utf-8

'''
You are given two arrays (without duplicates) nums1 and nums2 where nums1's elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
'''

#normal: 比较无脑的暴力遍历
#stack+dict(hashmap): 非常优雅的利用到了栈，每个元素入栈，如果当前元素大于栈顶元素
#  栈顶元素就找到了右边最近的大于它的值，添加到dict(hashmap)的映射关系
#  最后栈如果不为空，那说明这里面的元素的右边没有比它大的值，并且从栈顶到栈底是元素大小是递增

'''
Time complexity : O(m*n)
'''
def nextGreaterElement(nums1, nums2):
    end = len(nums2)
    ret = []
    for n in nums1:
        start = nums2.index(n)+1
        while start < end:
            if nums2[start]>n:
                ret.append(nums2[start])
                break
            start += 1
        if start == end:
            ret.append(-1)
    return ret


'''
Time complexity : O(m+n). 
 1.The entire numsnums array(of size n) is scanned only once.
 2.The stack's n elements are popped only once. 
 3.The findNums array is also scanned only once.
'''
def nextGreaterElement_stack(nums1, nums2):
    d,st = dict(), []
    for n in nums2:
        while st and st[-1]<n:
            d[st.pop()] = n
        st.append(n)

    ans = []
    for m in nums1:
        if m in d:
            ans.append(d[m])
        else:
            ans.append(-1)
    return ans


nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement_stack(nums1, nums2))