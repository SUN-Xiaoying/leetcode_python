# https://leetcode.com/problems/lfu-cache/description/
# HARD


class LFUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.list = []
        self.max_freq = 0
        self.capacity = capacity

    def get(self, key: int) -> int:


    def put(self, key: int, value: int) -> None:
        if map.containKeys(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)