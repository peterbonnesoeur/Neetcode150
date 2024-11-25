class Solution:
    # To REDO
    # def rob(self, nums: List[int]) -> int:
    #     def robHouse(array):
    #         if len(array) == 0:
    #             return 0
    #         if len(array) == 1:
    #             return array[0]
    #         else:
    #             return max(array[0] + robHouse(array[2:]), robHouse(array[1:]))

    #     return robHouse(nums)

    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
