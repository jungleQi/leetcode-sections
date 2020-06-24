'''
1.  Hashmap provides Insert and Delete in average constant time, although has problems with GetRandom.
    The idea of GetRandom is to choose a random index and then to retrieve an element with that index.
There is no indexes in hashmap, and hence to get true random value, one has first to convert hashmap
    keys in a list, that would take linear time.

2.  Array List has indexes and could provide Insert and GetRandom in average constant time, though has problems with Delete.
    To delete a value at arbitrary index takes linear time.
    The solution here is to always delete the last value:
        I.Swap the element to delete with the last one.
        II.Pop the last element out.
'''

#hashmap + list
#hashmap  key:num value:num index in list
#list     [num0, num1, ... ]

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            lastIdx, dstIdx = len(self.list) - 1, self.dict[val]
            self.dict[self.list[lastIdx]] = dstIdx
            self.list[lastIdx], self.list[dstIdx] = self.list[dstIdx], self.list[lastIdx]

            self.list.pop()
            del self.dict[val]

            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()