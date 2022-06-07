class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        memory = set()
        max_length, l = 0, 0

        for r in range(0, len(s)):
            while s[r] in memory:
                memory.remove(s[l])
                l += 1

            memory.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length