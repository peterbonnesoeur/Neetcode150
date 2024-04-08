class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]  # Each vertex is its own root initially
        self.rank = [1] * size  # Initialize ranks for union by rank optimization

    def find(self, x):
        # Path compression
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])  # Connect directly to the root
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
            
        uf = UnionFind(len(edges) + 1)
        result = []

        # To detect a cycle, we try to connect each edge and see if they're already connected
        for edge in edges:
            u, v = edge
            if uf.connected(u, v):
                # print(f"A cycle detected with the edge ({u} {v})")
                return edge
            else:
                uf.union(u, v)

        return result
