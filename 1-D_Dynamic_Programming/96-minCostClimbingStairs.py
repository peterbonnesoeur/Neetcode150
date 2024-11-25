class Solution:
    min_cost = 10_000_000

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def climbSteps(step_num: int, current_cost: int):
            if step_num > len(cost):
                # print("here")
                # current_cost += cost[val - 1]
                # print(step_num, cost, current_cost)
                if self.min_cost > current_cost:
                    self.min_cost = current_cost

            elif step_num <= len(cost):
                current_cost += cost[step_num - 1]
                # print(step_num, current_cost)
                climbSteps(step_num + 1, current_cost)
                climbSteps(step_num + 2, current_cost)

        climbSteps(1, 0)
        climbSteps(2, 0)
        return self.min_cost
