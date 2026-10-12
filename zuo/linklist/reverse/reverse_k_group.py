# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# Hard ???
from typing import Optional

from linklist.helper import ListNode, create_linked_list, print_list


class Solution:

    def team_end(self, start:ListNode, k:int):
        k -= 1
        while start and k>0:
            start = start.next
            k -= 1

        return start

    def reverse(self, start:ListNode, end:ListNode):
        cur = start
        end = end.next
        pre, temp = None, None
        while cur != end:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        start.next = end

    # TODO: Hand write it, Repeat
    # 1 ms Beats 42.66%
    def reverseKGroup (self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        end = self.team_end(head, k)
        if not end: return head

        head = end
        self.reverse(start, end)
        lastTeamEnd = start

        while lastTeamEnd.next:
            start = lastTeamEnd.next
            end = self.team_end(start, k)
            if not end: return head
            self.reverse(start, end)
            lastTeamEnd.next = end
            lastTeamEnd = start

        return head


    # 3 ms Beats 31.87%
    def reverseKGroup_container(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        if len(arr) < k : return head
        new_arr = []
        # Using Python's list slicing and range with a step
        # If chunk is full size k, reverse it
        #           arr.extend(chunk[::-1])
        for i in range(0, len(arr), k):
            chunk = arr[i:i+k]

            if len(chunk) == k:
                new_arr.extend(chunk[::-1])
            else:
                new_arr.extend(chunk)

        dummy = ListNode(0)
        cur = dummy

        for i in range(len(new_arr)):
            cur.next = ListNode(new_arr[i])
            cur = cur.next

        return dummy.next





s = Solution()
# 2 -> 1 -> 4 -> 3 -> 5
print_list(s.reverseKGroup(create_linked_list([1,2,3,4,5]), 2))
