class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        cumSum = 0
        maxR, maxL = 0, 0
        L = 0

        for R in range(len(nums)):

            if cumSum < 0:
                L = R
                cumSum = 0

            cumSum += nums[R]
            if cumSum > maxSum:
                print(L, R, cumSum)
                maxSum = cumSum
                maxL, maxR = L, R

        return maxSum
