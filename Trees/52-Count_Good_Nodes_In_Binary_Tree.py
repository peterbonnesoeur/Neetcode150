# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Here, we just need to ensure that on my path, I record the latest max and that my value is superior or equal to the current_max
class Solution:
    count = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        if root:
            self.traversal(root, root.val)
        
        return self.count
        
    def traversal(self, node, current_max):
        if node.val >= current_max:
            self.count+=1
            current_max = node.val
        
        if node.left:
            self.traversal(node.left, current_max)
        if node.right:
            self.traversal(node.right, current_max)