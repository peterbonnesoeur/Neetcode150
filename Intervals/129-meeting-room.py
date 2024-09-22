"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""



class Solution:

    def overlap(self, a: Interval, b: Interval) -> bool:
        return a.end > b.start

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) ==0:
            return True

        intervals = sorted(intervals, key=lambda x: x.start)

        current = intervals[0]
        for interval in intervals[1:]:
            if self.overlap(current, interval):
                return False
            current = interval
        return True