#2 pass algorithm. \
# The first pass is to find the new interval
#The second pass is to insert the new interval into the array.
class Solution:

    def overlap(self, a: List[int] , b: List[int])-> bool :
        return max(a[0], b[0]) - min(a[1], b[1]) <= 0

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        for i, interval in enumerate(intervals):
            if self.overlap(interval, newInterval):
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            else:
                res.append(interval)

        for i in range(len(res)):
            if res[i][0] > newInterval[0]:
                res.insert(i, newInterval)
                break
        else:
            res.append(newInterval)

        return res