
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort numbers to handle duplicates easily
        sorted_nums = sorted(nums)
        result = []
        self.backtrack(sorted_nums, 0, [], result)
        return result

    def backtrack(self, nums: List[int], start: int, path: List[int], result: List[List[int]]):
        # Add the current combination to the result
        result.append(path[:])  # Use path[:] instead of list(path) for a slight optimization
        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue
            # Include nums[i] in the subset and proceed to add more elements into the path
            self.backtrack(nums, i + 1, path + [nums[i]], result)  # Combine list operations
