# Honestly easy after doing word_search_2 ...
# Here, we just go through the board in a dfs fashion and explore further if there is a match.

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> List[str]:
        def dfs(x, y, word, i = 0):
            letter = board[x][y]
            to_search = len(word)

            if len(word) == i :
                # Found a word, add it to the result set.
                self.result.add(word)
                # Early stopping if all words are found.
                return True

            board[x][y] = '#'  # Mark the current cell as visited
            for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):  # Explore all directions
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == word[i]:
                    if dfs(nx, ny, word, i + 1):
                        break  # Early stopping if all words are found.
            board[x][y] = letter  # Backtrack
            return False  # Return false to continue searching.

        def buildTrie(word: str):
            root = {}
            node = root
            for letter in word:
                node = node.setdefault(letter, {})
            node['end'] = True
            return root

        self.result = set()
        trie = buildTrie(word)
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0] and dfs(x, y, word, i = 1):
                    break  # Early stopping if all words are found.

        return list(self.result)