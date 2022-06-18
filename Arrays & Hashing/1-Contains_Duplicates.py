# Usage of an hashmap to check if a list contains duplicates
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = set()

        for num in nums:
            if num in counter:
                return True
            counter.add(num)
        return False