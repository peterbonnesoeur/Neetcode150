# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
import string
from copy import deepcopy

class WordDictionary(object):

    def __init__(self):
        self.memory = set()
        self.word_level = defaultdict(set)
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.memory.add(word)
        mem = ""
        for depth, char in enumerate(word):
            mem += char
            self.word_level[depth + 1].add(mem)
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # if there are only 2 ways to add a ., I would just list them all...
        dot_locations = []
        for i,char in enumerate(word):
            if char == ".":
                dot_locations.append(i)
        
        if len(dot_locations) == 0:
            if word in self.memory:
                return True
        lowercase_letters = list(string.ascii_lowercase)

        if len(dot_locations) == 1:
            for char in lowercase_letters:
                index = dot_locations[0]
                to_match = word[:index] + char + word[index+1:]
                if to_match in self.memory:
                    return True

        if len(dot_locations) == 2:
            for char in lowercase_letters:
                for char_2 in lowercase_letters:
                    index = dot_locations[0]
                    to_match = word[:index] + char + word[index+1:]
                    index_2 = dot_locations[1]
                    to_match = to_match[:index_2] + char_2 + to_match[index_2+1:]
                    if to_match in self.memory:
                        return True

        return False
        
        
