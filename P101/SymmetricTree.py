# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:                 # If tree is empty, it's symmetric
            return True

        def isMirror(t1, t2):       # Helper function to check if two trees are mirrors
            if not t1 and not t2:    # Both nodes empty → symmetric
                return True
            if not t1 or not t2:     # One node empty → not symmetric
                return False
            if t1.val != t2.val:     # Values not equal → not symmetric
                return False
            # Check children: left of t1 vs right of t2, right of t1 vs left of t2
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root.left, root.right)  # Start with left and right subtree
