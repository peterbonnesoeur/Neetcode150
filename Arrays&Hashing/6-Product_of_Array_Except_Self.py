# The trick here is to use two passes -> complexity of O(n) means taht we can do two loops remember ?
# First, we compute the prodcut in the first pass, we keep the val of the first pas and mult withthe val.
# We do the same at the second pass
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        first_pass = 1
        for i in range(len(nums)):
            res[i] = first_pass
            first_pass *= nums[i]

        second_pass = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= second_pass
            second_pass *= nums[j]

        return res
