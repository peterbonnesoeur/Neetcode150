# To redo
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # I am dumb for not thinking about this...
        sums  = sum(nums)
        if sums%2:
            return False

        target = sum(nums)//2

        dp = set()
        dp.add(0)
        for i in range (len(nums)):
            nextDP = set()
            # Super simple when you thik about it since we just 
            # need to explore the begining of the state
            for t in dp:
                if (t+ nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        
        return False

        