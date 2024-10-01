class Solution:
        # q = deque()
        # wordSet = set(wordList)
        # for i, letter in enumerate(beginWord):
        #     if letter != endWord[i]:
        #         q.append([i, endWord[i]])


        # print(q)
        # def bfs(my_queue, current_word, current_depth = 0):
        #     new_queue = deque()

        #     while my_queue:
        #         i, letter = my_queue.pop()
        #         temp_word = copy(current_word)
        #         temp_word[i] = letter
        #         if temp_word in wordSet:
        #             res = max(0, bfs(my_queue + new_queue, temp_word), current_depth + 1)
        #         else:
        #             new_queue.append([i, letter])



    def _is_only_one_letter_dif(self, origin_word, new_word):

        count = 0
        for i, letter in enumerate(origin_word):
            if letter != new_word[i]:
                count +=1
            if count > 1:
                return False
        if count ==1 :
            return True


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def dfs(current_word, current_word_list, count=0):
            excluded_words = []
            to_check_words = []
            current_res = 0
            # print(count, current_word_list, current_word)
            for word in current_word_list:
                if self._is_only_one_letter_dif(current_word, word):
                    to_check_words.append(word)
                    if word == endWord:
                        # print("finished", count + 1)
                        return count + 1
                else:
                    excluded_words.append(word)



            if len(to_check_words) == 0:
                return 0

            for i,word in enumerate(to_check_words):
                res = dfs(word, to_check_words[:i] + to_check_words[i+1:] + excluded_words, count+1)
                if current_res == 0:
                    current_res = res
                elif res != 0:
                    current_res = min(current_res, res)

            return current_res

        # print(self._is_only_one_letter_dif("bat", "cat"))
        return dfs(beginWord, wordList, count=1)




