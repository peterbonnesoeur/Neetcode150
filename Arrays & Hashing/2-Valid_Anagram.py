# Use a counter for both words and check if differences

# Can also resort to array sorting to compare the anagrams
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for a in set(s):
            if s.count(a) != t.count(a):
                return False

        return True