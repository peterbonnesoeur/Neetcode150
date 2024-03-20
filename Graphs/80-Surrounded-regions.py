class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, visited):
            directions = [[-1,0], [0, -1], [1, 0], [0, 1]]
            visited.add((r,c))

            for direction in directions:
                new_r = r + direction[0]
                new_c = c + direction[1]

                if (new_r, new_c) in visited or (not 0<= new_r < ROWS) or (not 0<= new_c < COLS):
                    continue

                if board[new_r][new_c] == "O":
                    visited = dfs(new_r, new_c, visited)
            
            return visited

        visited = set()
        for r in range(ROWS):
            if board[r][0] == "O":
                visited = dfs(r, 0, visited)
            if board[r][COLS-1] == "O":
                visited = dfs(r, COLS-1, visited)

        for c in range(COLS):
            if board[0][c] == "O":
                visited = dfs(0, c, visited)
            if board[ROWS-1][c] == "O":
                visited = dfs(ROWS-1, c, visited)

        print(visited)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] =="O" and (r,c) not in visited:
                    board[r][c] = "X"

        return board
        

        
