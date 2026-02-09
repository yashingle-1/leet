from typing import Optional
from P101.SymmetricTree import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0  # store max diameter found

        def dfs(node):
            nonlocal diameter  # allows us to update outer variable
            if not node:
                return 0

            left = dfs(node.left)   # height of left subtree
            right = dfs(node.right) # height of right subtree

            diameter = max(diameter, left + right)  # update max diameter
            return 1 + max(left, right)             # return height of this node

        dfs(root)               # start DFS from root
        return diameter         # return the maximum diameter found
