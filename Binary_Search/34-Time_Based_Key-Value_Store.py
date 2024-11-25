# Usage of a tuple (timestamp, value) for autosorting with defaultdict
# Use a binary search to find the timestamp_pre <= timestamp

from collections import defaultdict


class TimeMap:
    def __init__(self):
        self._dict_val = defaultdict(list)
        self.dict_tmstmp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._dict_val[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        return self.binary_search(self._dict_val.get(key, []), timestamp)

    def binary_search(self, turples: list, timestamp: int) -> str:
        if len(turples) == 0:
            return ""

        l, r = 0, len(turples) - 1

        while l <= r:
            mid = (l + r) // 2

            if turples[mid][0] == timestamp:
                return turples[mid][1]

            if turples[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1

        mid = (l + r) // 2

        if turples[mid][0] <= timestamp:
            return turples[mid][1]
        else:
            return ""
