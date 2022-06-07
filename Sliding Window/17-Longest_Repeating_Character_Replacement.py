from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_length = 0
        memory = defaultdict(int)

        for r in range(len(s)):
            memory[s[r]] += 1
            if len(memory) > 1 and (sum(memory.values()) - max(memory.values())) > k:
                #print(memory, sum(memory.values()), max(memory.values()))
                memory[s[l]] -=1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length

