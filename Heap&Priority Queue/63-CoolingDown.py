class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        value_counts = Counter(tasks)
        total_num = len(value_counts)
        max_heap = [-val for val in value_counts.values()]
        heapify(max_heap)
       
        time = 0
        cooling_down = []
        while max_heap or cooling_down:
            time+=1
            if max_heap:
                cnt = heappop(max_heap) + 1
                if cnt != 0:
                    cooling_down.append([time + n, cnt])
            if cooling_down and cooling_down[0][0] == time:
                _, cnt = cooling_down.pop(0)
                heappush(max_heap, cnt)
        return time
            
