# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Basically, we go through each element of our BST and extract the list of sorted occurences to get the lowest value
class Solution:
    result = None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        results = []
        def smallest_path(node, k, current_loop = 0):
            if node.right and k >= current_loop:
                # This is just a small optimisation to not get too much into the right part of the branches since the graph is deep enough to do a search on k
                smallest_path(node.right, k, current_loop + 1)
            results.append(node.val)
            if node.left:
                smallest_path(node.left, k, current_loop + 1 )

            return
        if root:
            smallest_path(root, k)

        return results[-k]
