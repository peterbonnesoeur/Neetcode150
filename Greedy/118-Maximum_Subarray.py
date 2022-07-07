# The reasoning for this one is quite easy:
# a maximum subarray is achievedby saying that the maximum sum is allways achieved
# if I am superior to zero. Hence,the total needs to be reseted.
# At each reset, the array is being rewritten and we can achieve our alg
# in one go.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res