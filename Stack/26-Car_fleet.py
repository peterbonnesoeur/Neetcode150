# Use the speed metric. First, sort the vehicles
# 2 - Fill the stack with the time that each will take to reach the objective
# # - if the time taken by the latest element is inferior to the one ahead,remove the last element
# 4 - return the length of the stack

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair, reverse = True): # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)