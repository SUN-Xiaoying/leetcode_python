# https://leetcode.com/problems/partition-list/description/?envType=problem-list-v2&envId=linked-list
from typing import Optional

from helper import ListNode


class Solution:
    # 0ms Beats 100.00%
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None: return
        left_head, left_tail =  None, None
        right_head, right_tail = None, None
        _next = None

        while head is not None:
            _next = head.next
            head.next = None
            if head.val >= x:
                if right_head is None:
                    right_head = head
                else:
                    right_tail.next = head
                right_tail = head
            else:
                if left_head is None:
                    left_head = head
                else:
                    left_tail.next = head
                left_tail = head
            head = _next

        if left_head is None:
            return right_head
        left_tail.next = right_head
        return left_head

