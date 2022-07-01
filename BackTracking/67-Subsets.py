
# I am bad with these but we need to visualize this as a tree.

#With the first dfs, we decide to add the current num
# While the scond dfs maps the subsets in case i did not choose the number i

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i: int):

            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])

            dfs(i + 1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
