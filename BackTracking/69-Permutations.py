# Really complicated still to get the logic in my head but going there

from copy import deepcopy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        subset = []
        result = []
        def dfs(sub_array):
            if len(sub_array) == 0:
                result.append(deepcopy(subset))
                return

            for i in range(len(sub_array)):
                subset.append(sub_array[i])
                dfs(sub_array[:i] + sub_array[i+1:])
                subset.pop()

            return

        dfs(nums)
        return result