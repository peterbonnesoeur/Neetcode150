# Other approach using a tree-like structure:

# The treick here (memory-wise), is to impose a set of parameters.
# we on;y have lowercase words, hence 26 placeholders is more than enough in our case
# each placeholder can have a given child and we indicate that a whole word is stored with:
# a flag "end"

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] is None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:

        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return True






# Use two dict, one containing the actual word and the other one being a depth leveled defautdict containing a set at each level. Each time a word is recorded, it is decomposed for each level and add to the corresponding set.
# The search featue is then reusing this past knowledge by
#looking at the depth of the word and seeing if or word subset
# is stored in memory.



class Trie:

    def __init__(self):
        self.memory = set()
        self.word_level = defaultdict(set)

    def insert(self, word: str) -> None:
        self.memory.add(word)
        mem = ""
        for depth, char in enumerate(word):
            mem += char
            self.word_level[depth + 1].add(mem)

    def search(self, word: str) -> bool:
        return word in self.memory

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.word_level[len(prefix)]


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)