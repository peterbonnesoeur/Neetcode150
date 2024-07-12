# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# You may return the answer in any order.

# Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

class Solution:

    # Overlap function -> could be much simpler but I got lazy
    def overlap(self, a: List[int] , b: List[int])-> bool :
        return max(a[0], b[0]) - min(a[1], b[1]) <= 0


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        # we first need to sort the elements to get the minimum list length otherwise no can do.
        intervals = sorted(intervals, key=lambda x: x[0])

        while len(intervals) > 1:
            new_intervals = []
            current_item = intervals[0]
            # Basically, just check the current element vs the rest and then, redo a try on the previous list
            for interval in intervals[1:]:
                if self.overlap(current_item, interval):
                    current_item = [min(current_item[0], interval[0]) ,max(current_item[1], interval[1])]
                else:
                    new_intervals.append(interval)

            intervals = new_intervals
            res.append(current_item)

        return res + intervals
