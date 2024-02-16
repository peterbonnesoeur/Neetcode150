# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Pretty straightforward with recursion, we need to keep calling the system recursively and the results are actually quite good
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            # Empty trees are valid BSTs.
            if not node:
                return True

            # The current node's value must be within the range (low, high).
            if node.val <= low or node.val >= high:
                return False

            # Recursively validate the left and right subtree.
            # For the left subtree, set the upper limit to the current node's value.
            # For the right subtree, set the lower limit to the current node's value.
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root)
