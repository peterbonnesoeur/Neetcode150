import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_squarred(x: List[int]) -> int:
            distance = x[0] ** 2 + x[1] ** 2
            return distance, x

        distances = map(distance_squarred, points)
        res = heapq.nsmallest(k, distances, key=lambda x: x[0])
        return [x[1] for x in res]
