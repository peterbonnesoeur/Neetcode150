# Use the counter collections item to get the frequency of each character in the string

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in Counter(nums).most_common(k)]
