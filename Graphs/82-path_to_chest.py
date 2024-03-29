from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        current_paths = deque() # Queue for BFS

        # Initialize the queue with all the chests available
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    current_paths.append((r, c))

        # Directions for adjacent cells
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        path_to_chest = 0

        # BFS from the chest location
        while current_paths:
            for _ in range(len(current_paths)):  # Only expand the current level
                x, y = current_paths.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 2147483647:
                        grid[nx][ny] =  path_to_chest + 1
                        current_paths.append((nx, ny))
            path_to_chest += 1  # Increment time after one layer of spreading

        return grid