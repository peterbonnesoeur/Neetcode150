
# use a dfs kind of architecture and keep track of the current subset.
# Thehardest part here is tovisualize that this is an acceptance process by backtracking.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i: int, total : int):

            if total == target:
                res.append(subset.copy())
                return

            if i >= len(candidates) or total > target:
                return

            subset.append(candidates[i])

            # We accept the current element i and increment the perceived total
            dfs(i, total + candidates[i])
            subset.pop()
            #We do not accept the current element i and increment the perceived total
            dfs(i + 1, total)

        dfs(0, 0)
        return res