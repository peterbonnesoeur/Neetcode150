"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def overlap(self, a:Interval , b: Interval) -> bool:
        return a.end>b.start

    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals = sorted(intervals, key=lambda x: x.start)

        count_loop = 0
        while len(intervals)>=1:
            count_loop +=1
            current_item = intervals[0]
            new_intervals = []
            for interval in intervals[1:]:
                if self.overlap(current_item, interval):
                    if current_item.end > interval.end:
                        new_intervals.append(current_item)
                        current_item = interval
                    else:
                        new_intervals.append(interval)
                else:
                    current_item  = interval

            intervals = new_intervals

        return count_loop


# # Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

# class Solution:

#     # Overlap function -> could be much simpler but I got lazy
#     def overlap(self, a:List[int] , b: List[int]) -> bool:
#         return a[1]>=b[0]

#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         res = []

#         # we first need to sort the elements to get the minimum list length otherwise no can do.
#         intervals = sorted(intervals, key=lambda x: x[0])

#         while len(intervals) > 1:
#             new_intervals = []
#             current_item = intervals[0]
#             # Basically, just check the current element vs the rest and then, redo a try on the previous list
#             for interval in intervals[1:]:
#                 if self.overlap(current_item, interval):
#                     current_item = [min(current_item[0], interval[0]) ,max(current_item[1], interval[1])]
#                 else:
#                     new_intervals.append(interval)

#             intervals = new_intervals
#             res.append(current_item)

#         return res + intervals