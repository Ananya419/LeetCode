
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_val):
            if not node:
                return 0
            current_val = (current_val << 1) | node.val
            if not node.left and not node.right:  # leaf
                return current_val
            return dfs(node.left, current_val) + dfs(node.right, current_val)

        return dfs(root, 0)

# Example Usage:
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(1)
    solution = Solution()
    print(solution.sumRootToLeaf(root))  # Output: 22
    