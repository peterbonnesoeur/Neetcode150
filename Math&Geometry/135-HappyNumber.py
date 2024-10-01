class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            res = 0
            n_str = str(n)
            for num in n_str:
                res += int(num)**2
            if res in seen:
                return False
            else: 
                seen.add(res)
            n = res
        
        return True