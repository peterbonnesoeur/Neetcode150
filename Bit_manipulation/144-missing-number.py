
# Did not achieve this one. It should not be a bit probleme I think
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
