class Solution:
    def jump(self, nums: List[int]) -> int:
        cumSum = 0
        maxL, maxR = 0, 0
        L = 0

        if len(nums) == 1:
            # Tough edge case here -> if we are already at the end, no need to jump
            return 0

        count_jump = 0
        for R in range(len(nums)):
            # First case: check if the position R is impossible to reach
            if L + nums[L] < R:
                break
            # Second case: check if I have more potential to reach further away at position R
            if R + nums[R] > L + nums[L]:
                print("here")
                count_jump += 1
                L = R

            if R + nums[R] >= len(nums) - 1:
                return count_jump + 1
