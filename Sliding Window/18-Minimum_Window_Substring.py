def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        if len(t) == 0:
            return ""

        if s == t:
            return s


        if len(t) > len(s):
            return ""

        if s == t:
            return s

        l = 0
        res = (-1, -1)
        min_length = float('inf')

        t_count = Counter(t)
        window_count = {}


        for r in range(len(s)):
            window_count[s[r]] = 1 + window_count.get(s[r], 0)
            flag = True

            while flag:
                flag = False
                #temp = s[l:r+1]
                for item in t_count.keys():
                    if t_count[item] > window_count.get(item, 0):
                        break

                else:
                    flag = True
                    if (r - l + 1) <=  min_length:
                        res = (l, r)
                        min_length = r - l + 1
                    window_count[s[l]] = window_count.get(s[l], 0) - 1
                    l += 1


        l, r = res
        return s[l:r + 1] if l != -1 else ""