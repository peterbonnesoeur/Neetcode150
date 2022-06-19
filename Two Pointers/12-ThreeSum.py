# Same as TwoSum, 1 - sort, 2 - main for loop (first third number), 3- if the sum is greater than target, decrement the right pointer, 4- if the sum is less than target, increment the left pointer, 5- if the sum is equal to target, return the pair of indices
# 6 - if the value of the l pointer is allways the same (anmd to remove duplicates, iterate as long the val is the same.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()



        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue


            l, r = i+1, len(nums) - 1
            while l < r:
                three_sum = a + nums[r] + nums[l]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    results.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1

        return results
