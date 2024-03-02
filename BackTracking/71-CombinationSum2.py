# Dummy version

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Sort to handle duplicates and make the combination process easier.

        def dfs(start, path, target):
            # Base case: if the target is zero, we've found a combination
            if target == 0:
                result.append(path)
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # If the number is greater than the target, break the loop
                if candidates[i] > target:
                    break

                # Continue with the next number and reduce the target
                dfs(i + 1, path + [candidates[i]], target - candidates[i])

        # Start the DFS with an empty path and the whole array
        dfs(0, [], target)
        return result



# Optimised version with early stopping and usingtarget as a memory for the objective to attain:

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Sort to handle duplicates and make the combination process easier.

        def dfs(start, path, target):
            # Base case: if the target is zero, we've found a combination
            if target == 0:
                result.append(path)
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # If the number is greater than the target, break the loop
                if candidates[i] > target:
                    break

                # Continue with the next number and reduce the target
                dfs(i + 1, path + [candidates[i]], target - candidates[i])

        # Start the DFS with an empty path and the whole array
        dfs(0, [], target)
        return result