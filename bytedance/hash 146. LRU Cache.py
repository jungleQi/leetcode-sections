import collections
class LRUCache:

    def __init__(self, capacity):
        self.od = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)

        self.od[key] = value
        if len(self.od) > self.capacity:
            self.od.popitem(last=False)