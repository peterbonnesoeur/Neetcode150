class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        ROWS, COLS  = len(heights), len(heights[0])
        pac, alt = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            for direction in directions:
                dfs(r+direction[0], c+direction[1], visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, alt, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, alt, heights[r][COLS-1])

        res = []

        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in alt:
                    res.append([i,j])

        return res
        

        
