#coding=utf-8
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

#key point:
def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    n = len(nums)
    i = n - 1

    # 从后向前遍历，i是 第一个变小的数索引，还是首次下降之前的最高点索引，这个微妙的不同
    # 会让后续操作陷入corner case的泥潭

    # i是第一个变小的数索引
    # 这样处理，麻烦在于如果i==0，会有两种可能性：3,2,1 or 2,3,1
    # 因为i的含义是将要做逆转的索引值，即便结束定位，后面还要判断是否真的是要做逆转的索引值
    '''
    while i>0:
        if nums[i]>nums[i-1]:
            i -= 1
            break
        i -= 1
    '''

    # i的含义是从尾部向头部遍历时的首次最高点索引
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    # 如果最高点不是端点，首先做两个元素的交换
    if i > 0:
        j = n - 1
        # 从尾部开始查找第一个比待交换元素大的值
        while nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

    # 做区域的逆转
    k = 0
    for k in range((n - i) // 2):
        nums[i + k], nums[n - k - 1] = nums[n - k - 1], nums[i + k]