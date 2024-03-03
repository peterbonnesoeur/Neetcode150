class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        subset = []
        def dfs(sub_array):
            if len(sub_array)==0:
                return
            if sub_array == sub_array[::-1]:
                result.append(list(subset) + [sub_array])
            for i, _ in enumerate(sub_array):
                # print(i)
                left_array = sub_array[:i+1]
                if left_array == left_array[::-1]:
                    subset.append(left_array)
                    dfs(sub_array[i+1:])
                    subset.pop()

        dfs(s)
        return result
    
