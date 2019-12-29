'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
'''

#利用两个栈实现一个队列非常elegant
#一个output栈用于pop/peek，另一个input栈用于push
#利用peek的时机，如果output栈为空，依次将input元素出栈，然后入栈output。如果output非空，就直接返回output栈顶
#push直接入栈input；pop，先peek一次。input和output都非空，队列queue就非空

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.input.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.output.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.input and not self.output

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
print(param_2)
param_3 = obj.pop()
print(param_3)
param_4 = obj.empty()
print(param_4)

obj.push(4)
param_3 = obj.peek()
print(param_3)
param_2 = obj.pop()
print(param_2)


