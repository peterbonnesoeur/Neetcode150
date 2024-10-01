class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        maxlen = 0

        if len(text1)> len(text2):
            temp = text1
            text1 = text2
            text2 = temp

        #Map the universe and take the max recursively
        # This is a great way to do dp with matrixes
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        last_found = 0
        # offset = 0
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                  dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[0][0]
                