
#Using regex
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_str = re.sub(r'[^\w]|[\_]', '', s).lower()
        length_str = len(processed_str)
        for i in range(length_str):
            if i >= length_str - i:
                break
            if processed_str[i] != processed_str[length_str-i-1]:
                return False

        return True


#Using pointers :
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True

# Shortest one :
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS= [i.lower() for i in s if i.isalnum()]
        return newS == newS[::-1]