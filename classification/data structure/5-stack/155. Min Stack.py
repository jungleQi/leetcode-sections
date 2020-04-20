#coding=utf-8

'''
Design a 5-stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto 5-stack.
pop() -- Removes the element on top of the 5-stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the 5-stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''

#KEY: retrieving the minimum element in constant time.
#为了在常数时间，获取栈内最小元素，需要单独维护一个栈，从栈底到栈顶保持递增，即栈顶元素总是最小的
#在每次Pop和push时，s1按照列表正常方式处理，s2需要维护好，保证push到栈内的元素是递减的，Pop时，是否需要对s2也做出栈处理

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)
        if not self.s2 or self.s2[-1]>x:
            self.s2.append(x)

    def pop(self):
        """
        :rtype: None
        """
        top = self.s1.pop()
        if top == self.s2[-1]:
            self.s2.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.s2[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.pop()
obj.push(2)
obj.push(-1)
obj.push(1)
print(obj.top())
print(obj.getMin())