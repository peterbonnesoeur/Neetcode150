class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        matrix = [[False] * len(t) for i in range(len(s))]

        for i in range(len(t)):
            for j in range(len(s)):
                if t[i] == s[j]:
                    matrix[j][i] = True

        res = [0]

        def dfs(r, c):
            for i in range(r, len(s)):
                if matrix[i][c] == True:
                    if c < len(t) - 1:
                        dfs(i+1, c+1)
                    else:
                        res[0] +=1

        dfs(0,0)

        return res[0]