# https://leetcode.com/problems/copy-list-with-random-pointer
# Medium

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # TODO: Use O(N) memory space
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':


    # 40 ms Beats 66.00%
    def copyRandomList_HashSet(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}

        cur = head
        while cur:
            copies[cur] = Node(cur.val)
            cur = cur.next

        for node, copy in copies.items():
            copy.next = copies[node.next] if node.next else None
            copy.random = copies[node.random] if node.random else None

        return copies[head]