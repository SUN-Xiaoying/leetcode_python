# 链表往往都是很简单的算法问题，考察核心也不是算法设计，而是coding
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Helper to create list from array for testing
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

# Helper to print linked list
def print_list(node):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print(" -> ".join(vals))


def build_cycle_list(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    cur = head
    cycle_node = None

    for i in range(1, len(values)):
        new_node = ListNode(values[i])
        cur.next = new_node
        cur = new_node

        if i == pos:
            cycle_node = new_node

    # If pos == 0, cycle starts at head
    if pos == 0:
        cycle_node = head

    # Create cycle if pos != -1
    if pos != -1:
        cur.next = cycle_node

    return head
