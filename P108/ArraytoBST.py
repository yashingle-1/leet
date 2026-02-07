# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from typing import List
from P101.SymmetricTree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Helper function to build BST from subarray nums[left:right+1]
        def build(left, right):
            if left > right:            # Base case: no elements to process
                return None             # Return None for empty subtree

            mid = (left + right) // 2   # Choose middle index
            node = TreeNode(nums[mid])  # Create root node with middle element

            node.left = build(left, mid - 1)   # Recursively build left subtree
            node.right = build(mid + 1, right) # Recursively build right subtree

            return node                 # Return the node as root of this subtree

        return build(0, len(nums) - 1)       # Start with entire array