class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cumSum = 0
        maxL, maxR = 0, 0
        L = 0

        for R in range(len(nums)):

            if L + nums[L] < R:
                # print("here", L, nums[L], R)
                break
            if R + nums[R] >= L + nums[L]:
                # print("reset", L, nums[L], R, nums[R])
                L = R

            if R + nums[R] >= len(nums) - 1:
                return True

        return False
