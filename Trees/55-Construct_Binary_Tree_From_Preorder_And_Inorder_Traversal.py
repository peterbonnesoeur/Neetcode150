# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    root = None
    preorder_list = []
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # inorder_listdict = {inorder[i]:i for i in range(len(inorder))}
        inorder_dict = {inorder[i]:i for i in range(len(inorder))}

        def arrayToTree(left,right):
            if left > right:
                return None

            # pop the first root element
            root_value  = preorder.pop(0)
            root = TreeNode(root_value)

            # The main teaching here is to understand that the root element is a pivot point
            split_index = inorder_dict[root_value]

            # This part empties the left-side part of the preorder list
            root.left = arrayToTree(left, split_index - 1)

            # The remaining right side components
            root.right = arrayToTree(split_index + 1, right)

            return root


        return arrayToTree(0,len(preorder) - 1)

