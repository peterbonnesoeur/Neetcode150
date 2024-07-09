# basically a brute force approac.

# We are walking through the island andremembering when we are visiting a peculiar node of the island
# This solution is although quite slow.
class Solution:
    class Graph:
        def __init__(self, grid : List[List[str]], island = "1" ):
            self.grid = grid
            self.island = island
            self.row_number = len(grid)
            self.col_number = len(grid[0])
            self.visited = [[False for j in range(len(self.grid[0]))] for i in range(len(self.grid))]


        def isSafe(self, i, j):
            return (i >= 0 and i < self.row_number and
                    j >= 0 and j < self.col_number and
                    not self.visited[i][j] and self.grid[i][j] == self.island)

        def dfs(self, i, j):
             # These arrays are used to get row and
            # column numbers of 4 neighbours
            # of a given cell (We do not consider the diagonal cases)

            rowNbr = [-1, 1, 0, 0]
            colNbr = [0, 0, -1, 1]
            # Mark this cell as visited
            self.visited[i][j] = True

            # Recur for all connected neighbours
            for k in range(len(rowNbr)):
                if self.isSafe(i + rowNbr[k], j + colNbr[k]):
                    self.dfs(i + rowNbr[k], j + colNbr[k])

        def countIsland(self):
            count = 0
            for i in range(self.row_number):
                for j in range(self.col_number):
                    if self.visited[i][j] == False and self.grid[i][j] == self.island:
                        self.dfs(i, j)
                        count += 1

            return count

    def numIslands(self, grid: List[List[str]]) -> int:
        graph = self.Graph(grid)
        count = graph.countIsland()

        return count

# Similar solution where the grid for visited nodes is replaced by a set:

def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == "0" or
                (r, c) in visit):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands