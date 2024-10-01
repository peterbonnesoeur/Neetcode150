# Redo: I do not get how to approach those.......

from collections import defaultdict
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {} #(r, c) : v

        ROWS = len(matrix)
        COLS = len(matrix[0])

        def dfs(r, c, preVal):
            # print(r,c, preVal, (matrix[r][c] <= preVal))
            if not (0<=r<ROWS) or not (0<=c<COLS) or (matrix[r][c] <= preVal):
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]


            currVal = matrix[r][c]
            res = 1
            res = max(res, 1 + dfs(r -1,c,currVal))
            res = max(res, 1 + dfs(r + 1,c,currVal))
            res = max(res, 1 + dfs(r,c - 1,currVal))
            res = max(res, 1 + dfs(r,c + 1,currVal))
            
            dp[(r,c)] = res
            return res
        

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,-1)
        return max(dp.values()) 
