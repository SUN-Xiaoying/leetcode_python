# https://leetcode.com/problems/merge-two-sorted-lists/description/
from typing import Optional
from heap.helper import create_linked_list, print_list, ListNode

class Solution:
    # 0 ms Beats 100.00%
    # Eazy一遍过，不错不错
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head

        cur1, cur2 = list1, list2

        while cur1 and cur2:
            if cur1.val < cur2.val:
                tail.next=cur1
                tail=tail.next
                cur1=cur1.next
            else:
                tail.next = cur2
                tail = tail.next
                cur2 = cur2.next

        while cur1:
            tail.next = cur1
            tail = tail.next
            cur1 = cur1.next
        while cur2:
            tail.next = cur2
            tail = tail.next
            cur2 = cur2.next

        return head.next


s = Solution()
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
print_list(s.mergeTwoLists(create_linked_list([1,2,4]),create_linked_list([1,3,4])))