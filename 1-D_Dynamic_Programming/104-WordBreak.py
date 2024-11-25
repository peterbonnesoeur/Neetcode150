# We want to know if, until one point, there was a solution
# Whichever the solution was, before moving forth
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # I have to get used to this structure. I had some
        # "Math issues" with the indexes here
        dp = [0] * (len(s) + 1)
        for i in range(len(s) + 1):
            for word in wordDict:
                if len(word) < i + 1:
                    if word != s[i - len(word) : i]:
                        continue

                    if len(word) == i:
                        dp[i] = 1
                    elif dp[i - len(word)]:
                        dp[i] = 1
        # print(dp)
        return dp[-1] == 1
