# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# pick the maximum distance from left and right while keeping a memory (res) of the max distance internodes

# Res does not perturbate the distances computations.

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        _, res = self.dfs(root, res)

        return res

    def dfs(self, root, res) :
        if not root:
            return (-1, res)
        left, res = self.dfs(root.left, res)
        right, res = self.dfs(root.right, res)
        res = max(res, 2 + left + right)

        return (1 + max(left, right), res)