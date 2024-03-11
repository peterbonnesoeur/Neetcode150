from collections import deque, defaultdict
from functools import partial
import heapq

class Twitter:
    # tweets = defaultdict(partial(deque, maxlen=10))
    # follow_who = defaultdict(set)
    # ts = 0

    def __init__(self):
        self.tweets = defaultdict(partial(deque, maxlen=10))
        self.follow_who = defaultdict(set)
        self.ts = 0
        pass


    def postTweet(self, userId: int, tweetId: int) -> None:
        # print(self.tweets)
        self.tweets[userId].append([tweetId, self.ts])
        self.ts -= 1
        return



    def getNewsFeed(self, userId: int) -> List[int]:
        whole_tweets = list(self.tweets[userId])
        # print(whole_tweets, self.tweets)

        for followee in self.follow_who[userId]:
            whole_tweets.extend(self.tweets[followee])
        if len(whole_tweets)==0:
            return []
        # print(whole_tweets)

        res = heapq.nsmallest(10, whole_tweets, key= lambda x: x[1])
        return [x[0] for x in res]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_who[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_who[followerId].discard(followeeId)
