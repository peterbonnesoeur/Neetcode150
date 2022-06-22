

# Basic binary search where we converge to the point of dirependcy.
# when l == r, we know that we reached the end goal.
def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        k = 0

        while l < r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:
                r = mid - 1
            # right sorted portion
            else:
                l = mid + 1

        return nums[l]


#Using the 2 pointer methodology:
# 1- init pointers
# 2 - update the value of the pointers depending on their value
# 3 - Update the value of k only when nums[l] > nums[r] since we want to know
#4 - where the rotation is happening and hence,when the breakage point is
def findMin(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    k = 0

    while l < r:
        if nums[l] > nums[r]:
            k = r
            r -= 1
        else:
            l += 1

    return nums[k]