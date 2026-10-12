# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
# Med
import random

# 124 ms Beats 65.67%
class RandomizedSet:

    def __init__(self):
        self.cnt = 0
        self.set = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.set.keys():
            return False
        self.set[val] = self.cnt
        self.arr.append(val)
        self.cnt += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set.keys() or not self.set:
            return False
        idx = self.set[val]
        last_val = self.arr[-1]

        # switch
        self.set[last_val] = idx
        self.arr[idx] = last_val

        # clean
        self.arr.pop()
        self.set.pop(val)
        self.cnt -= 1
        return True

    def getRandom(self) -> int:
        r = random.randint(0,self.cnt-1)
        return self.arr[r]

obj = RandomizedSet()
# true
print(obj.insert(1))
# false
print(obj.remove(2))
# true
print(obj.insert(2))
# random
print(obj.getRandom())
# True
print(obj.remove(1))
# False
print(obj.insert(2))