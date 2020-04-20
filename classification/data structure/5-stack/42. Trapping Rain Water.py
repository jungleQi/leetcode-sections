#coding=utf-8

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

#native: 1.每个idx都入栈，如果栈顶高度小于当前高度，就出栈，循环下去，直至栈空或者栈顶高度大于当前高度
#        2.如果栈被清空，需要计算以栈底为左边界，当前元素为右边界这个区间的trap总和
#        3.如果结束遍历，栈非空，经过前面数次比较之后，此时左边界非常靠谱，是最高的，
#          所以从右边界依次向左遍历，直至栈底指向索引。可以将遍历过程中的最高边界作为可以达到的最高边界
#          将当前元素高度与最高边界做差值，就是这次能够累积的trap。

#5-stack: 1.保持栈内的元素高度递降，如果当前元素大于栈顶元素指向高度，就弹出栈顶top，记住栈顶元素高度，依据该高度产生的
#         delta，这里delta= 当前元素和新的栈顶元素中较小的值 - 弹出的栈顶元素高度，
#         需要累加的元素N = 当前索引到新的栈顶元素索引之间元素个数，新增的trap=delta*N
#       2.当前元素索引入栈


def trap_twoPointer(height):
    stack = []
    traps = 0
    for i,h in enumerate(height):
        left = -1
        while stack and height[stack[-1]] < h:
            left = stack.pop()

        if not stack and left != -1:
            right = i-1
            while right>left:
                traps += height[left]-height[right]
                right -= 1
        stack.append(i)

    if stack:
        left  = stack[0]
        right = stack[-1]
        maxHeight = height[right]
        while left < right:
            if height[right] < maxHeight:
                traps += maxHeight-height[right]
            else:
                maxHeight = height[right]
            right -= 1

    return traps

def trap_stack(height):
    current, ans = 0, 0
    stack = []

    for i,h in enumerate(height):
        while stack and h > height[stack[-1]]:
            top = stack.pop()
            if not stack: break

            dist = i-stack[-1]-1
            addHeight = min(height[stack[-1]], h) - height[top]
            ans += addHeight * dist

        stack.append(i)

    return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap_stack(height))