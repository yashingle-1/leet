from typing import Optional
from P101.SymmetricTree import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]   # store node and current depth
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)  # update max depth

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth


# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:                # If tree is empty, depth is 0
#             return 0
#         # depth of current node = 1 + max(depth of left, depth of right)
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
