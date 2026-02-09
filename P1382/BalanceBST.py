from P101.SymmetricTree import TreeNode
class Solution:
    def balanceBST(self, root):

        arr = []

        # Step 1: Inorder traversal → sorted values
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)

        # Step 2: Build balanced BST
        def build(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            node = TreeNode(arr[mid])

            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)

            return node

        return build(0, len(arr) - 1)
