class MedianFinder:
    def __init__(self):
        self.bottom_heap = []
        self.top_heap = []

    def addNum(self, num: int) -> None:
        median = self.findMedian()
        if median == None:
            heappush(self.top_heap, num)
            return
        if num >= median:
            heappush(self.top_heap, num)
        else:
            heappush(self.bottom_heap, -num)

        if len(self.bottom_heap) - len(self.top_heap) > 1:
            heappush(self.top_heap, -heappop(self.bottom_heap))
        elif len(self.top_heap) - len(self.bottom_heap) > 1:
            heappush(self.bottom_heap, -heappop(self.top_heap))
        return

    def findMedian(self) -> float:
        size_top_heap = len(self.top_heap)
        size_bottom_heap = len(self.bottom_heap)
        if size_top_heap == 0 and size_bottom_heap == 0:
            return None

        if size_top_heap > size_bottom_heap:
            return self.top_heap[0]
        elif size_top_heap < size_bottom_heap:
            return -self.bottom_heap[0]
        else:
            return (self.top_heap[0] - self.bottom_heap[0]) / 2
