#Slow solution
#
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        l = 0
        for r in range(len(s2) + 1):
            if r - l == len(s1):
                if(sorted(s2[l:r]) == s1):
                    return True
                l+=1

        return False

# Much faster solution:

# Here we try to mathc the counter and at the exit of the window, we replenish it

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr = Counter(s1)
        w = len(s1)
        match = len(cntr)

        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0:
                    match-=1
            # replenish the counter
            if i >= w and s2[i-w] in cntr:
                cntr[s2[i-w]] += 1
                match +=1

            if all([cntr[i] == 0 for i in cntr]):
                return True
        return False


# Optimised sol - Leetcode


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
