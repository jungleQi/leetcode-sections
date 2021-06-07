'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
'''

'''
#高度降低了，将前面高的推平
#当前高度入栈

算法一：
# × stack未被判断的元素到当前新加入元素的rec面积 -> 会超时
[N，N-1, ... 1] 会退化成O(n²)

===》 演变算法，降低时间复杂度：

算法二：
# stack 升序
# 出现降低高度，就只计算stack[top]覆盖rectangle的面积
'''

def largestRectangleArea(heights):
    heights.append(0)
    stack = [-1]
    res = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            res = max(res, h * w)
        stack.append(i)
    return res

arr = [2,1,5,6,2,3]
print(largestRectangleArea(arr))