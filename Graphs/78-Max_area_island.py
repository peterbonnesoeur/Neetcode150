class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        max_area = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        # DFS approach which is not the most optimized approach there, instead of diving deep and retrieving the graph, using a bfs whohc looks first at all the neighboors makes this 
        # more efficient
        def dfs(r, c):
            if ( not 0 <= r < rows or not 0 <= c < cols or
                grid[r][c] == 0 or
                (r, c) in visit):
                return 0

            visit.add((r, c))
            current_area = 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                current_area += dfs(r + dr, c + dc)
            return current_area

        # Better space complexity approach, same computational complexity but more straightforward and better res
        def bfs(r, c):
            q = deque([(r, c)])
            visit.add((r, c))
            area = 1
            while q:
                row, col = q.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visit:
                        visit.add((nr, nc))
                        q.append((nr, nc))
                        area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(bfs(r, c), max_area)
        return max_area