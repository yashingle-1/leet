# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right    
from typing import Optional
from P101.SymmetricTree import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True   # Empty subtree is valid

            # Current node must lie inside allowed range
            if not (low < node.val < high):
                return False

            # Left subtree → values must be smaller than node.val
            # Right subtree → values must be greater than node.val
            return (
                dfs(node.left, low, node.val) and
                dfs(node.right, node.val, high)
            )

        # Start with infinite range
        return dfs(root, float("-inf"), float("inf"))