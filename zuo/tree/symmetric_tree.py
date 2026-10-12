# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/
from collections import deque
from typing import Optional

from tree.utils import build_tree_from_list, TreeNode


class Solution:
    # Your runtime beats 100.00 % of python3 submissions.
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def is_mirror(left:Optional[TreeNode], right:Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root.left, root.right)

if __name__ == "__main__":
    sol = Solution()
    tree = build_tree_from_list([1,2,2,3,4,4,3])
    tree1 = build_tree_from_list([1,2,2,None,3,None,3])
    print(sol.isSymmetric(tree))
    print(sol.isSymmetric(tree1))