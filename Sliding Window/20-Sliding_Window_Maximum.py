class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i in range(len(nums)):
            # the first/left (max) element is out of the current window
            if q and i - q[0] == k:
                q.popleft()

            while q:
                # pop useles elements from last/right of the queue
                if nums[q[-1]] < nums[i]:
                    q.pop()
                else:
                    break

            q.append(i)

            if i >= k-1: # i == k-1 is the beginning of a full window
                result.append(nums[q[0]])

        return result