# Usage of the properties of the XOR operator


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a = a^num
        return a