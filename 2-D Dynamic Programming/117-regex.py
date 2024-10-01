class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        matrix = [[False]*(len(p) +1)  for i in range(len(s) + 1)]
        matrix[-1][-1] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                match =  i < len(s) and (s[i] == p[j] or p[j] == ".")

                if (j+1) < len(p) and p[j+1] == "*":
                    # ignore the number
                    matrix[i][j] = matrix[i][j+2]
                    if match:
                        matrix[i][j] = matrix[i+1][j] or matrix[i][j]
                elif match:
                    matrix[i][j] = matrix[i+1][j + 1]
        return matrix[0][0]
        

       
    def isMatch_(self, s: str, p: str) -> bool:
        # Too many conditions and I did not get that c* can match "ccccc", "c" or "" which messed the system
        dp = {}

        # matrix = [[False]*len(p) for i in range(len(s))]

        def dfs(s_, p_, preVal):
            print(s_,p_,preVal)
            if (s_, p_) in dp:
                return dp[(s_, p_)]
            
            if len(p_) == 0 and len(s_)!=0:
                return False
            elif len(p_) == 0 and len(s_) == 0:
                return True
            elif len(s_) == 0 and p_ == ".*":
                return True
            elif len(s_) == 0 and len(p_) !=0:
                return False

            # preVal = None
            finished_p, finished_s = False,False
            for i in range(len(s_)):
                finished_s = (i == len(s_)-1)
                if i>=len(p_):
                    finished_p = False
                print(i, len(p_), finished_p)
                for j in range(i, len(p_)):
                    finished_p = (j == len(p_)-1)
                    if s_[i] == p_[j]:
                        preVal = p_[j]
                        break
                    elif p_[j] == ".":
                        preVal = p_[j]
                        break
                    elif p_[j] == "*":
                        # print("here", s_[i], preVal)
                        if (s_[i] == preVal) or (preVal == "."):
                            dp[(s_, p_)] =  (dfs(s_[i+1:], p_[j:], preVal) or dfs(s_[i+1:], p_[j+1:], preVal) or dfs(s_[i:], p_[j+1:], preVal))
                            # print(s_, p_, dp[(s_, p_)], dfs(s_[i+1:], p_[j:], preVal) , dfs(s_[i+1:], p_[j+1:], preVal), dfs(s_[i:], p_[j+1:], preVal))
                            return dp[(s_, p_)]
                        else:
                            # Consider the case where * matches 0 characters
                            dp[(s_, p_)] = dfs(s_[i:], p_[j+1:], preVal)
                            return dp[(s_, p_)]
                    else:
                        dp[(s_, p_)] = False
                        return False
                    
            print(finished_s, finished_p)

            dp[(s_, p_)] = finished_s and finished_p
            return dp[(s_, p_)]
        
        return dfs(s,p, None)

