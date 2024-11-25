class Solution:
    def hasher(self, nums: List[int]) -> str:
        return "#".join([str(num) for num in nums])

    def scoreMaker(self, i: int, nums: List[int]):
        if len(nums) == 0:
            return 0
        res = 1
        for i in range(i - 1, i + 2):
            if 0 <= i < len(nums):
                res *= nums[i]

        return res

    def maxCoins(self, nums: List[int]) -> int:

        dp = {}

        def dfs(numbers: List[int]):
            if len(numbers) == 0:
                return 0

            hashed_numbers = self.hasher(numbers)

            if hashed_numbers in dp:
                return dp[hashed_numbers]

            res = -float("inf")
            for i in range(len(numbers)):
                res = max(
                    res,
                    self.scoreMaker(i, numbers) + dfs(numbers[:i] + numbers[i + 1 :]),
                )

            dp[hashed_numbers] = res
            return res

        dfs(nums)
        # print(dp)
        return max(dp.values())
