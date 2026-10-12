# https://leetcode.com/problems/merge-k-sorted-lists/description/
# Hard
from heapq import heapify
from typing import List, Optional
import heapq

from heap.helper import create_linked_list, print_list, ListNode

class Solution:

    def heapinsert(self, arr: List[ListNode], i: int):
        while i > 0 and arr[i].val < arr[(i - 1) // 2].val:
            arr[(i - 1) // 2], arr[i] = arr[i], arr[(i - 1) // 2]
            i = (i - 1) // 2

    def heapify(self, arr: List[ListNode], i: int):
        l = i * 2 + 1
        size = len(arr)
        while l < size:
            best = l + 1 if l + 1 < size and arr[l + 1].val < arr[l].val else l
            if arr[best].val < arr[i].val:
                arr[best], arr[i] = arr[i], arr[best]
                i = best
                l = i * 2 + 1
            else: break

    def heappush(self, minheap: List[ListNode], item: ListNode):
        minheap.append(item)
        self.heapinsert(minheap, len(minheap) - 1)

    def heappop(self, minheap: List[ListNode]):
        if not minheap:
            return None

        minheap[0], minheap[-1] = minheap[-1], minheap[0]
        item = minheap.pop()

        if minheap:
            self.heapify(minheap, 0)

        return item

    # 27 ms Beats 18.92%
    # TODO: 别用 heapq
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head
        minheap = []

        for h in lists:
            if h:
                self.heappush(minheap,h)

        while minheap:
            node = self.heappop(minheap)
            tail.next = node
            tail = tail.next

            if node.next:
                self.heappush(minheap, node.next)

        return head.next


    # 9ms Beats 69.39%
    def mergeKLists_best(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        head = ListNode(0)
        # 头部生成小根堆
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minheap, (node.val, i, node))  # (val, index, node)

        dummy = ListNode(0)
        current = dummy

        while minheap:
            val, i, node = heapq.heappop(minheap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(minheap, (node.next.val, i, node.next))

        return dummy.next

# Create input: list of linked lists
input_lists = [[1,4,5],[1,3,4],[2,6]]
linked_lists = [create_linked_list(lst) for lst in input_lists]

s = Solution()
# [1,1,2,3,4,4,5,6]
print_list(s.mergeKLists(linked_lists))

