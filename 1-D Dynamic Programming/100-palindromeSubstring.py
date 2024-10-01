class Solution:
    def countSubstrings(self, s: str) -> int:
        res = ""
        resLen = 0
        count_palyndrome = 0
        for i in range(len(s)):

            l,r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                count_palyndrome +=1
                l-=1
                r+=1
            
            l,r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                count_palyndrome +=1
                l-=1
                r+=1
        return count_palyndrome