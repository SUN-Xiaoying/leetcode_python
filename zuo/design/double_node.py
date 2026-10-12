class DoubleNode:
    def __init__(self, key="", val=0, last=None, next=None):
        self.key = key
        self.val = val
        self.last = last
        self.next = next

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, new_node: DoubleNode):
        if not new_node:
            return
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.last = self.tail
            self.tail = new_node

    def move_to_tail(self, node: DoubleNode):
        # 我总是忘记边界？
        # 边界就是放在最后加的

        if self.tail == node:
            return

        # 先断开 node
        if self.head == node:
            self.head = node.next
            self.head.last = None
        else:
            # node 在中间某处
            node.last.next = node.next
            node.next.last = node.last

        # 再把 node 链接到 tail
        node.last = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node

    def remove_head(self):
        if not self.head:
            return None
        # 为什么要单独讨论头尾相等
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.last = None

        temp.next = None
        temp.last = None

        return temp



# --- Helper Function for Testing ---
def verify_list(dl, description):
    print(f"--- {description} ---")

    # Forward Pass
    current = dl.head
    forward = []
    while current:
        forward.append(str(current.key))
        current = current.next
    print(f"Forward : {' -> '.join(forward)}")

    # Backward Pass (Crucial for Doubly Linked Lists)
    current = dl.tail
    backward = []
    while current:
        backward.append(str(current.key))
        current = current.last
    print(f"Backward: {' <- '.join(backward)}")
    print("-" * 30)


# --- EXECUTION ---

# Setup
dl = DoubleList()
node_a = DoubleNode("A", 1)
node_b = DoubleNode("B", 2)
node_c = DoubleNode("C", 3)
node_d = DoubleNode("D", 4)

dl.add_node(node_a)
dl.add_node(node_b)
dl.add_node(node_c)
dl.add_node(node_d)

verify_list(dl, "Initial State (A -> B -> C -> D)")
dl.move_to_tail(node_c)
verify_list(dl, "After moving Middle(C) to Tail")