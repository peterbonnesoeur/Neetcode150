# Redo
# BAsically, make it a path exercise.
# Update the next state with True and have a starter state.
# I tried Implementing it with a depth search but this is not keeping
# The ordering of the string in mind


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        if len(s1) == 0:
            if s2 == s3:
                return True
            else:
                return False

        if len(s2) == 0:
            if s1 == s3:
                return True
            else:
                return False

        dp = [[False] * (len(s2) + 1) for i in range((len(s1) + 1))]
        dp[0][0] = True

        # We want to go to the extremities of the field (in case we want to fully )
        # Complete with a previous one
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i < len(s1):
                    if s1[i] == s3[i + j] and dp[i][j]:
                        dp[i + 1][j] = True

                if j < len(s2):
                    if s2[j] == s3[i + j] and dp[i][j]:
                        dp[i][j + 1] = True
        # print("final", dp)
        return dp[-1][-1]
