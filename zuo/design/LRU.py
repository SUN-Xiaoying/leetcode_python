# https://leetcode.com/problems/lru-cache/description/
# MEDIUM
from design.double_node import DoubleNode, DoubleList


# 双链表 + 哈希表
# 最新的在尾部
# 145 ms Beats 47.74%
class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.node_list = DoubleList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map.keys():
            node = self.map.get(key)
            self.node_list.move_to_tail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            node = self.map.get(key)
            node.val = value
            self.node_list.move_to_tail(node)
        else:
            if len(self.map) == self.capacity:
                self.map.pop(self.node_list.remove_head().key)

            new_node = DoubleNode(key, value)
            self.map[key] = new_node
            self.node_list.add_node(new_node)

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))