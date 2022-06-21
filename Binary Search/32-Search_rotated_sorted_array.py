#Brute force:
# 1- find rotation axis
# 2 - binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        k = 0

        while l < r:
            if nums[l] > nums[r]:
                r -= 1
                k = r + 1
            else:
                l += 1

        new_nums = nums[k:] + nums[:k]

        l, r = 0, len(new_nums) - 1

        while l <= r:
            m = l + ((r - l) // 2) # (l + r) // 2 can lead to overflow
            if new_nums[m] > target:
                r = m - 1
            elif new_nums[m] < target:
                l = m + 1
            else:
                return (m + k)%len(nums)

        return -1

#Smarter way

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1