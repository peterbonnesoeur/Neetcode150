# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = defaultdict(int)
        if root:
            self.traversal(root, result)

        result_list = [val for key, val in sorted(result.items(), key = lambda i: i[0])]
        return result_list


    def traversal(self, node, result,  current_depth = 0):
        if current_depth not in result.keys():
            result[current_depth] = node.val

        if node.right:
            self.traversal(node.right, result, current_depth + 1)
        if node.left:
            self.traversal(node.left, result, current_depth + 1)