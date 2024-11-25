# Create a Hahsmap,and check if target - key is in the map, else add traget - key to the map


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for id, item in enumerate(nums):
            if target - item in prevMap:
                return [prevMap[target - item], id]
            prevMap[item] = id

        return []
