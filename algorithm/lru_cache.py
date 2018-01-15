from collections import deque


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.max_cap = capacity
        self.cap = 0
        self.cache = {}
        self.q = deque()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = self.cache.get(key)
        if val:
            self.q.remove(key)
            self.q.append(key)
            return val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        val = self.cache.get(key)
        if val is not None:
            self.q.remove(key)
            self.cap = self.cap - 1

        if val is None and self.cap == self.max_cap:
            q_key = self.q.popleft()
            del self.cache[q_key]
            self.cap = self.cap - 1

        self.q.append(key)
        self.cache[key] = value
        self.cap = self.cap + 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # returns 1
cache.put(3, 3)  # evicts key 2
print(cache.get(2))  # returns -1 (not found)
cache.put(4, 4)  # evicts key 1
print(cache.get(1))  # returns -1 (not found)
print(cache.get(3))  # returns 3
print(cache.get(4))  # returns 4
