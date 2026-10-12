# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
from collections import deque
from typing import Optional, List

from tree.utils import TreeNode, build_tree_from_list


class Solution:
    # 0ms Beats 100.00%
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #   L -> R-1
        #   R-1 -> L
        # q_len = R-L
        if not root: return []
        r, l=0, 0
        reverse = False
        queue = deque([root])
        r+=1
        ans =[]
        while r>l:
            q_len = r - l
            level=[]
            i = l if not reverse else r-1
            j = 1 if not reverse else -1
            k = q_len
            while k:
                level.append(queue[i].val)
                i+=j
                k-=1

            # 遍历
            for _ in range(q_len):
                node = queue[l]
                l += 1
                if node:
                    if node.left:
                        queue.append(node.left)
                        r += 1
                    if node.right:
                        queue.append(node.right)
                        r += 1

            ans.append(level)
            reverse = not reverse

        return ans


if __name__ == "__main__":
    sol = Solution()
    # [[3],[20,9],[15,7]]
    tree = build_tree_from_list([3,9,20,None,None,15,7])
    # tree = build_tree_from_list([1,2])
    print(sol.zigzagLevelOrder(tree))