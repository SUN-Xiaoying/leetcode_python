#
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
#
from typing import Optional
from tree.utils import TreeNode, build_tree_from_list


# You are here!
# Your runtime beats 100.00 % of python3 submissions.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    sol = Solution()
    tree = build_tree_from_list([1, 2, 3, 4, 5])
    print(sol.maxDepth(tree))
