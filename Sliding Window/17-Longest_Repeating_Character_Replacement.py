#create a dictionary with a memory of the iteration of each character. If thedifference between the sum of the values contained in the window and
# the maximum of the memory value is superior to k, then, decreise the window size.

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

