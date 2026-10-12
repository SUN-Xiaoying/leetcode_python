# https://leetcode.com/problems/maximum-frequency-stack/
# HARD
from linklist.helper import ListNode

# 95ms Beats 37.29%
class FreqStack:

    def __init__(self):
        self.times_map = {}
        self.history_list = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val in self.times_map.keys():
            times = self.times_map.get(val) + 1
            self.times_map[val] = times
            self.max_freq = max(self.max_freq, times)
            if times not in self.history_list:
                self.history_list[times] = []
            self.history_list[times].append(val)
        else:
            self.times_map[val] = 1
            if 1 not in self.history_list:
                self.history_list[1] = []
            self.history_list[1].append(val)

    def pop(self) -> int:
        result = self.history_list[self.max_freq].pop()
        if len(self.history_list[self.max_freq]) == 0:
            self.max_freq -= 1
        times = self.times_map[result]
        self.times_map[result] = times - 1
        return result

# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
# 5, 7, 5, 4
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
# param_2 = obj.pop()