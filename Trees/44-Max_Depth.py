# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Simple solution, recursive algorithm that iterates on left and right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        else:
            left = 1
            right = 1

            if root.left:
                left += self.maxDepth(root.left)
            if root.right:
                right += self.maxDepth(root.right)
            depth = max(left, right)

        return depth

#Fancier approach:
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)