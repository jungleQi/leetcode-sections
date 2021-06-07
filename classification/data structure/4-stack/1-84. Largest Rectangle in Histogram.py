'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
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