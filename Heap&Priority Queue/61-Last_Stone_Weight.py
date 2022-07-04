import heapq

## Same principle as an heap, but this time with a maxHeap.
# To implement a maxheap, simply use negative values instead of positive ones.
# AKA: inverse the values.

class Solution:
    def lastStoneWeight_(self, stones: List[int]) -> int:
        length = len(stones)
        stones = [-x for x in stones]
        heapify(stones)

        while length > 1:
            dif = heappop(stones) - heappop(stones)

            if dif != 0:
                heappush(stones, dif)
                length -=1
            else:
                length -=2

        if length == 0:
            return 0
        else:
            return -stones.pop()