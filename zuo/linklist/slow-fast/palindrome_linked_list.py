# https://leetcode.com/problems/palindrome-linked-list/description/
# Easy ???
from typing import Optional

from linklist.helper import ListNode, create_linked_list, print_list


class Solution:
    # 38 ms Beats 40.77%
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    # 快慢指针？是否成环
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return True
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tail = self.reverse(slow)
        slow, fast = head, tail
        while fast:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next

        return True


    # 12 ms Beats 97.53%
    def isPalindrome_stack(self, head: Optional[ListNode]) -> bool:
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        cur = head
        while stack:
            if cur.val != stack.pop():
                return False
            cur = cur.next

        return True


s = Solution()
# True
print(s.isPalindrome(create_linked_list([1])))
# True
print(s.isPalindrome(create_linked_list([1,2,2,1])))
# False
print(s.isPalindrome(create_linked_list([1,2,2])))