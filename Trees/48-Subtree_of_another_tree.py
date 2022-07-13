# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Run a check if same node in cas

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        elif root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        else:
            return True and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
