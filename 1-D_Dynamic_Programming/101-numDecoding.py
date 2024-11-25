class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                (s[i] == "1") or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]

        return dp[0]

    def numDecodings_(self, s: str) -> int:

        if s.startswith("0"):
            return 0

        keys = set([str(i) for i in range(1, 27)])
        count = 1
        preMade = 0

        for i in range(len(s)):
            if s[i] in keys:
                pass

            if i >= 1 and s[i] == "0":
                if int(s[i - 1 : i + 1]) > 26:
                    return 0
                else:
                    print("here")
                    count -= 1
                    if preMade:
                        count -= 1
                        preMade = 0

            if i >= 1 and s[i - 1 : i + 1] in keys:
                print("Add", s[i - 1 : i + 1])
                count += 1
                if preMade >= 2:
                    preMade
                    count += 1
                preMade = 1
            else:
                preMade = False
        return max(count, 0)
