#coding=utf-8

'''
Given a circular array (the next element of the last element is the first element of the array),
print the Next Greater Number for every element.

The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to 6-search circularly, which is also 2.
'''

#4-stack：1.循环数组，并不是说最后一个元素等于第一个元素，而是逻辑定义上的循环，为了便于遍历循环数组
#       ，将数组追加到它自己尾部，行程一个新的数组
#       2.追加之前的原始数组中每个元素都做一次入栈，当前遍历元素比栈顶元素大，栈顶元素获得Next Greater Number，被认领出栈。
#       所以，栈顶到栈底的元素是递增。

def nextGreaterElements(nums):
    stack = []
    N = len(nums)
    ret = [-1] * N

    for i, num in enumerate(nums + nums):
        while stack and nums[stack[-1]] < num:
            ret[stack[-1]] = num
            stack.pop()
        if (i < N):
            stack.append(i)

    return ret

nums = [5,4,3,2,1]
print(nextGreaterElements(nums))
