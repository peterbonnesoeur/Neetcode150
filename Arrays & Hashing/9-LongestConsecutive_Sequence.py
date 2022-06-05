class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        originalSet = set(nums)

        longest = 0

        for num in originalSet:
            # check that we have a starting point
            if (num - 1) not in originalSet:
                length = 1
                while(num + length in originalSet):
                    length +=1
                longest = max(length, longest)

        return longest