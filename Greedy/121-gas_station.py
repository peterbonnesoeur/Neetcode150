class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        maxSum=-1
        L=0
        cumSum = 0
        maxL = -1


        for R in range(2*len(cost)):
            if cumSum<0:
                cumSum=0
                L=R
            if L >= len(cost):
                return -1

            cumSum+=gas[R%len(cost)]
            cumSum-=cost[R%len(cost)]
            if cumSum>maxSum:
                maxSum=cumSum
                maxL = L
                # MaxR = R
        return maxL