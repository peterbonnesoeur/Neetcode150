# use a sorting function to find the anagrams and add them to a dictionnary where the key is the sorted anagram and the val is the non sorted anagram.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagrams = {}
        for i in strs:
            t = "".join(sorted(i))

            if t in dict_anagrams:
                dict_anagrams[t].append(i)

            else:
                dict_anagrams[t] = [i]

        return list(dict_anagrams.values())
