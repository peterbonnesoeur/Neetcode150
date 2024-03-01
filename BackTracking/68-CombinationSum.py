
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

# A better and slicker solution
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(array, current_sum):
            for i,item in enumerate(array):
                test = current_sum + item

                if test > target:
                    continue
                elif test == target:
                    result.append(list(subset) + [item])
                    continue

                subset.append(item)

                # we can consider only the
                dfs(array[i:], test)
                subset.pop()

        dfs(sorted(set(candidates)),0)
        return result