class Solution:
    def maxArea(self, height: List[int]) -> int:
        r, l = 0, len(height) - 1
        max_water = 0

        while r < l:
            water_capacity = min(height[r], height[l])*(l - r)
            max_water = max(max_water, water_capacity)

            if height[r] < height[l]:
                r +=1
            else:
                l -=1

        return max_water