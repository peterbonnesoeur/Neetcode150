# The goal here it to not limit opurselves to the present array
#We do abinary search to find the most optimal valueunder which, koko can eat bananas
# under h hours.

# 1 - set boundaries (0, max(piles))
# 2 - compute in between eating speed
#3 - compute the total time for kok to eat everythiong
# If the time is to big,increase the lower bound
# if the time is to small, decrease the upper bound

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = len(piles)

        l, r = 0, max(piles)

        while l <= r:

            m = (l + r) // 2

            total_time = 0
            print(m, l, r)
            for pile in piles:
                total_time += (((pile - 1)//m) + 1)

            if total_time <= h:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res