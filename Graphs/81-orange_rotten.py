
## NAive DFS solution -> not really well adapted to our issue
## Since we are 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = {}
        ROWS  = len(grid)
        COLS = len(grid[0])


        def dfs(r, c, visited, time = 0):
            directions = [[-1,0], [0, -1], [1, 0], [0, 1]]
            if (r,c) in visited.keys():
                visited[(r,c)] = min(visited[(r,c)], time)
            else:
                visited[(r,c)] = time

            for direction in directions:
                new_r = r + direction[0]
                new_c = c + direction[1]

                if (not 0<= new_r < ROWS) or (not 0<= new_c < COLS):
                    continue
                
                if (new_r, new_c) in visited.keys() and visited[(r,c)] < time:
                    continue
    
                if grid[new_r][new_c] == 1:
                    visited = dfs(new_r, new_c, visited, time+1)
            
            return visited


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visited = dfs(r,c, visited, 0)

        print(visited)
        max_time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if (r,c) not in visited.keys():
                        return -1
                    else:
                        max_time = max(max_time, visited[(r,c)])
        
        return max_time


# MUUUUUCH. better solution. For propagation and diffusion, BFS is the way yo go after all.
# This approach also uses the original board to propagate the new state directly within the original board
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        rotten = deque()  # Queue for BFS

        # Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))

        # Directions for adjacent cells
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes_passed = 0

        # BFS from all rotten oranges
        while rotten and fresh > 0:
            for _ in range(len(rotten)):  # Only expand the current level
                x, y = rotten.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # Make it rotten
                        fresh -= 1
                        rotten.append((nx, ny))
            minutes_passed += 1  # Increment time after one layer of spreading

        return minutes_passed if fresh == 0 else -1