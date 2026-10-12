# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional

from helper import ListNode


class Solution:
    # 0ms Beats 100.00%

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before = None
        temp = head
        after = temp

        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        head = before

        return head
