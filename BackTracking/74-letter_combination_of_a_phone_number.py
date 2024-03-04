class Solution:
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def letterCombinations(self, digits: str) -> List[str]:
        
        subset = []
        result = []
        len_digits = len(digits)

        def dfs(index):
            if index >= len_digits:
                result.append("".join(subset))
                return
            for i, item in enumerate(self.mapping.get(digits[index], [])):
                subset.append(item)
                dfs(index + 1)
                subset.pop()
            return
        
        if len(digits)>0:
            dfs(0)
        return result