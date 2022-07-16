# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Run a search through the tree. In case bit the left and right get
# an element found, we have the lowest notde in the tree
# if the current node is one of the val, look at the right and the left and
# return the current node.

class Solution:
    res = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root or not p or not q:
            return None

        self.search(root, p, q)
        return self.res

    def search(self, root, p, q):
        if not root:
            return False
        mid = left = right = False

        if root.val == p.val or root.val == q.val:
            mid = True

        right = self.search(root.right, p, q)
        left = self.search(root.left, p, q)
        if mid:
            if right or left:
                self.res = root

        elif left and right:
            self.res = root

        return mid or right or left