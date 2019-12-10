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


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack_1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())

        ret = self.stack_2.pop()

        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

        return ret


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())

        ret = self.stack_2.pop()
        self.stack_1.append(ret)

        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

        return ret

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack_1

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


