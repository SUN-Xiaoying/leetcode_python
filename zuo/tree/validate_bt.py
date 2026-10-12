#
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
#
from typing import Optional

from tree.utils import TreeNode, build_tree_from_list


class Solution:
    #   5
    #  / \
    # 1   6
    #    /
    #   4   <- This node violates the BST property (4 < 5), but your code won't catch it.
    def isValidBST_wrong(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is not None and root.left.val >= root.val:
            return False
        if root.right is not None and root.val >= root.right.val:
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

    # You are here!
    # Your runtime beats 100.00 % of python3 submissions.
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node: Optional[TreeNode], min_value: float, max_value: float) -> bool:
            if node is None:
                return True
            if not (min_value < node.val < max_value):
                return False
            return helper(node.left, min_value, node.val) and helper(node.right, node.val, max_value)

        return helper(root, -float('inf'), float('inf'))


if __name__ == "__main__":
    sol = Solution()
    tree = build_tree_from_list([5,4,6,None,None,3,7])
    print(sol.isValidBST(tree))