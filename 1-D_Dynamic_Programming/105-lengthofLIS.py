class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            j = i - 1
            currMax = 0
            while j >= 0:
                if nums[i] > nums[j]:
                    currMax = max(dp[j], currMax)
                    # break
                j -= 1
            dp[i] += currMax
        # print(dp)
        return max(dp)
