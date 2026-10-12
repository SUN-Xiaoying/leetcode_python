# https://leetcode.com/problems/linked-list-cycle/
# Easy
from typing import Optional

from linklist.helper import ListNode, build_cycle_list


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


    # 50 ms Beats 44.01%
    def hasCycle_hash_set(self, head: Optional[ListNode]) -> bool:
        positions = {}
        cur = head
        pos = 0
        while cur:
            if cur in positions:
                return True
            positions[cur] = pos
            pos +=1
            cur = cur.next

        return False




s = Solution()
# True
print(s.hasCycle(build_cycle_list([3,2,0,-4], 1)))
# False
print(s.hasCycle(build_cycle_list([1], -1)))