# https://leetcode.com/problems/linked-list-cycle-ii/
from typing import Optional

from linklist.helper import ListNode


class Solution:
    # 53 ms Beats 16.24%
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: return None
        slow = head.next
        fast = head.next.next
        while slow != fast:
            if not fast.next or not fast.next.next: return None
            slow = slow.next
            fast = fast.next.next
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow