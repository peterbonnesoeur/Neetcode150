class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1

        i = len(nums)



        if target == nums[int(i/2)]:
            return int(i/2)
        elif i == 1:
            return -1
        elif target < nums[int(i/2)]:
            return self.search(nums[:int(i/2)], target)

        elif target > nums[int(i/2)]:
            temp_res =  self.search(nums[int(i/2):], target)
            return int(i/2) + temp_res if temp_res != -1 else -1

        return res