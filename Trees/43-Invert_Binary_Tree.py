# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# For each node, verify if not null, else inverse left and right.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return

        if root.left is not None or root.right is not None:
            root.left, root.right = root.right, root.left
            self.invertTree(root.right)
            self.invertTree(root.left)

        return root