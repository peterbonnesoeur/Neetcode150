class Solution:

    # Overlap function -> could be much simpler but I got lazy
    def overlap(self, a: List[int] , b: List[int])-> bool :
        return max(a[0], b[0]) - min(a[1], b[1]) < 0
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # we first need to sort the elements to get the minimum list length otherwise no can do.
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)

        # while len(intervals) > 1:
        new_intervals = []
        current_item = intervals[0]
        # Basically, just check the current element vs the rest and then, redo a try on the previous list
        for interval in intervals[1:]:
            print(current_item, interval)
            if self.overlap(current_item, interval):
                print("here")
                if current_item[-1] > interval[-1]:
                    current_item = interval
            else:
                new_intervals.append(interval)
                current_item  = interval

        new_intervals.append(current_item)

        return len(intervals) - len(new_intervals)


