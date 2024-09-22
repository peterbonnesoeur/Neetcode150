from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_counted = Counter(s)
        # untouched_keys = set(s_counted.keys())
        touched_keys = set()
        result = []
        count = 0
        for i in range(len(s)):
            count+=1
            val = s[i]
            touched_keys.add(s[i])
            count_val = s_counted.get(val)
            if count_val == 1:
                touched_keys.remove(s[i])
            s_counted[val] = count_val - 1
            if len(touched_keys) == 0:
                result.append(count)
                count = 0
        return result