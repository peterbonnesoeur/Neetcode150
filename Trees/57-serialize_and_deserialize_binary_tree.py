# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# METHOD 1: super duper basic. Memory efficient
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def treeToArray(node):
            my_array = []
            if node:
                my_array.append(str(node.val))

                if node.left:
                    my_array += treeToArray(node.left)
                else:
                    my_array.append("")

                if node.right:
                    my_array += treeToArray(node.right)
                else:
                    my_array.append("")
            return my_array

        tree_to_array = treeToArray(root)

        return ",".join(tree_to_array)


    def deserialize(self, data):
        """Decodes your encoded data to tree.


        :type data: str
        :rtype: TreeNode
        """

        data_array = data.split(",")

        def arrayToTree():
            if len(data_array)>0:
                input_element = data_array.pop(0)
                if len(input_element) == 0:
                    return None

                node = TreeNode(int(input_element))

                if len(data_array) > 0:
                    node.left = arrayToTree()

                if len(data_array)> 0:
                    node.right = arrayToTree()
                return node

            else:
                return None

        return arrayToTree()






# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
