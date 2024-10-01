from collections import defaultdict
class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i,total)]

            dp[(i, total)] = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])

            return dp[(i, total)]
        
        return backtrack(0,0)
            

    # Cannot work since we get into the context window issue where the context window is max(nums)**len(nums)
    def findTargetSumWaysMemoryNotWorking(self, nums: List[int], target: int) -> int:
        abs_target = abs(target + 1)*3 
        dp = [0] * (abs_target *2 + 1)
        dp[abs_target] = 1

        targets = range(-abs_target, abs_target + 1)

        for num in nums:
            new_dp = [0] * (abs_target *2 + 1)
            print(dp)
            print(new_dp)
            for goal in targets:
                if abs(goal-num) <= abs_target:
                    master = goal - num
                    # print(abs_target - (goal - num))
                    new_dp[abs_target- goal] += dp[abs_target - master]
            
                if abs(goal + num) <= abs_target:
                    master = goal + num
                    new_dp[abs_target- goal] += dp[abs_target - master]
                #     new_dp[abs_target + goal] += dp[abs_target + num ]
            
            dp = new_dp
        
        print("final", dp, target + abs_target)
        return dp[target + abs_target]