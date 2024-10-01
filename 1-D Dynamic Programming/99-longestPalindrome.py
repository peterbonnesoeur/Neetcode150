class Solution:


    def longestPalindrome(self, s: str) -> str:
       
        #same lenght:
        res = ""
        resLen = 0

        for i in range(len(s)):
            l, r = i,i

            while l>=0 and r<len(s) and s[l] == s[r]:

                if r - l + 1> resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1

            #pair 
            l, r = i,i+1

            while l>=0 and r<len(s) and s[l] == s[r]:
                if r - l + 1> resLen:
                    resLen = r-l+1
                    res = s[l:r + 1]
                l -= 1
                r += 1
        return res





    def _isPalindrome(self, s:str):
        return s == s[::-1]
    def longestPalindrome_(self, s: str) -> str:
       
        def palindromeSearch(s):
            if len(s) == 1:
                return s
            elif self._isPalindrome(s):
                return s
            else:
                res1 = palindromeSearch(s[1:])
                res2 = palindromeSearch(s[:-1])
                if len(res1)> len(res2):
                    return res1
                else:
                    return res2
        
        return palindromeSearch(s)

