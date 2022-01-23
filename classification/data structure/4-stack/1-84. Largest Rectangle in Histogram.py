'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
'''

def largestRectangleArea(heights):
    #两个初始化能让整个处理流程变得连贯
    heights.append(0)
    stack = [-1]

    res = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            top = stack.pop()
            h = heights[top]

            #选择 i-stack[-1]-1 而不是 i-top 是实现整个贪婪算法的灵魂
            w = i - stack[-1] - 1

            res = max(res, h * w)
        stack.append(i)
    return res

#arr = [2,1,5,6,2,3]
arr = [2,1,2]
print(largestRectangleArea(arr))