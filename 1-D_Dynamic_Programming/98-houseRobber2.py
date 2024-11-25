class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums[:-1]:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        currentMax = rob2

        rob1, rob2 = 0, 0
        for num in [nums[-1]] + nums[:-2]:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return max(rob2, currentMax)
