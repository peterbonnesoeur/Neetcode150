"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from copy import deepcopy
from typing import Optional
class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        if node in self.visited:
            return self.visited[node]

        cloned_node = Node(node.val)
        self.visited[node] = cloned_node

        for neighbor in node.neighbors:
            cloned_node.neighbors.append(self.cloneGraph(neighbor))

        return cloned_node

# We maintain a dictionary self.visited to keep track of original nodes and their corresponding cloned nodes.
# When cloning a node, we first check if the node has already been visited. If it has, we return the cloned node associated with it from the self.visited dictionary.
# If the node has not been visited, we create a new cloned node, add it to the dictionary, and recursively clone its neighbors.