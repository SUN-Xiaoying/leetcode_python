# https://leetcode.com/problems/linked-list-random-node/description
import random
from typing import Optional

from linklist.helper import ListNode

# 8ms Beats 84.36%
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        self.size = 0
        current = head
        while current is not None:
            self.arr.append(current.val)
            self.size += 1
            current = current.next

    def getRandom(self) -> int:
        return self.arr[random.randrange(0, self.size)]
