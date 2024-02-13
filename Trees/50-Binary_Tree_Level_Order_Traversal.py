# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None0):
#         self.val = val
#         self.left = left
#         self.right = right

#basic solution using recursive defauldict and storing the depth as we traverse the tree
from collections import defaultdict
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        result_dict = defaultdict(list)
        result = []
        if root:
            self.depth_finder(root, result_dict)

        result = [val for key, val in sorted(result_dict.items(), key = lambda i: i[0])]
        return result

    def depth_finder(self, node, result_dict, current_depth = 0):
        result_dict[current_depth].append(node.val)
        if node.left:
            self.depth_finder(node.left, result_dict, current_depth + 1)
        if node.right:
            self.depth_finder(node.right, result_dict, current_depth + 1)

# a more memory efficient solution using a queue

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            length_level = len(queue)
            current_level = []

            for level in range(length_level):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result