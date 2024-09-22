class Solution:
    def overlap(self, a:List[int] , b: List[int]) -> bool:
        return a[1]>=b[0]

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        res = []

        # we first need to sort the elements to get the minimum list length otherwise no can do.
        intervals = sorted(intervals, key=lambda x: x[0])
        lengths = [interval[1] - interval[0] + 1 for interval in intervals]

        for query in queries:
            # Basically, just check the current element vs the rest and then, redo a try on the previous list
            min_size = -1
            for index, interval in enumerate(intervals):
                if interval[0] <= query <= interval[1]:
                    if min_size == -1:
                        min_size = lengths[index]
                    else:
                        min_size = min(lengths[index], min_size)

            res.append(min_size)

        return res