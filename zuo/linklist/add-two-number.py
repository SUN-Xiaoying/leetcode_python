# https://leetcode.com/problems/add-two-numbers/description/
# https://www.bilibili.com/list/8888480?sid=3509640&oid=659355657&bvid=BV1bh4y1r75d
from typing import Optional

from helper import ListNode

class Solution:
    # 3ms Beats 72.53%
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left, right = None, None
        carry = 0

        while l1 is not None or l2 is not None:
            sum =  (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry # Mistake without ()

            carry = sum//10
            val = sum%10

            if left is None:
                left = ListNode(val)
                right = left
            else:
                right.next = ListNode(val)
                right = right.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if carry:
            right.next=ListNode(1)

        return left
