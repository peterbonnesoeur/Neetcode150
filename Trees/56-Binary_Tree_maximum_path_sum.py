# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# The trick here is noticing that:
# 1- the output is a number, so we can just retrun a number
# 2 - take the max of the 3 use case for the local result: node, node+ right, node+ left
# 3 - In case node.val < 0, store the maximum between max(right, left, right + left + node) in a separated global variable
# I could definitely have made this cleaner now that I am phrasing it like this but oh well ^^'
class Solution(object):
    glob_res = []
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.glob_res = []
        if root:
            max_path = self.maxPathLocal(root)
            return max([max_path] + self.glob_res)
        else:
            return 0

    def maxPathLocal(self, node):
        local_result = 0
        if node:
            sum_best_path_left, sum_best_path_right = 0,0

            local_result = node.val
            if node.left:
                sum_best_path_left = self.maxPathLocal(node.left)
                if (node.val + sum_best_path_left) > node.val:
                    local_result = node.val + sum_best_path_left
                    if node.val < 0:
                         self.glob_res.append(sum_best_path_left)
                else:
                    self.glob_res.append(sum_best_path_left)

            if node.right:
                sum_best_path_right = self.maxPathLocal(node.right)
                if (node.val + sum_best_path_right) > node.val and sum_best_path_right > sum_best_path_left:
                    local_result = node.val + sum_best_path_right
                    if node.val < 0:
                         self.glob_res.append(sum_best_path_right)
                else:
                    self.glob_res.append(sum_best_path_right)

            if sum_best_path_right > 0 and sum_best_path_left > 0:
                self.glob_res.append(sum_best_path_right + sum_best_path_left + node.val)

            return local_result
        else:
            return 0



#CLEANER VERSION (MUCH WOW)


# The trick here is noticing that:
# 1- the output is a number, so we can just retrun a number
# 2 - take the max of the 3 use case for the local result: node, node+ right, node+ left
# 3 - In case node.val < 0, store the maximum between max(right, left, right + left + node) in a separated global variable
class Solution(object):
    glob_res = []
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.glob_res = []
        if root:
            max_path = self.maxPathLocal(root)
            return max([max_path] + self.glob_res)
        else:
            return 0

    def maxPathLocal(self, node):
        if node:
            sum_best_path_left, sum_best_path_right = 0,0
            local_max = node.val
            if node.left:
                sum_best_path_left = self.maxPathLocal(node.left)
                if node.val < 0:
                    self.glob_res.append(sum_best_path_left)

                local_max = max(node.val, node.val + sum_best_path_left)

            if node.right:
                sum_best_path_right = self.maxPathLocal(node.right)
                if node.val < 0:
                    self.glob_res.append(sum_best_path_right)

                local_max = max(local_max, node.val + sum_best_path_right)

            if (sum_best_path_right>0 and sum_best_path_left> 0):
                self.glob_res.append(node.val + sum_best_path_left + sum_best_path_right)

            return local_max
        else:
            return 0
