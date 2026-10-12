# https://leetcode.com/problems/intersection-of-two-linked-lists/description
# Easy
from typing import Optional

from linklist.helper import ListNode


class Solution:
    # 长链表先走diff，一定会同时相遇
    # 76 ms Beats 91.59%
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        diff = 0
        curA, curB = headA, headB
        while curA.next:
            curA = curA.next
            diff+=1
        while curB.next:
            curB = curB.next
            diff-=1

        curA, curB = headA, headB
        if diff>0:
            for i in range(diff):
                curA = curA.next
        else:
            for i in range(-diff):
                curB = curB.next

        while curA != curB:
            curA = curA.next
            curB = curB.next

        return curA

s = Solution()
print(s.getIntersectionNode())




