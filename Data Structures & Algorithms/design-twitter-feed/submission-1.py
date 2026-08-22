class Twitter:

    def __init__(self):
        self.tweet_map = defaultdict(list) # userId -> list of (timestamp, tweetIds)
        self.follow_map = defaultdict(set) # userId -> a set of followeeId
        self.timer = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        users_to_check = self.follow_map[userId] | {userId}

        # start each relevant user's pointer at their most recent tweet
        for uid in users_to_check:
            if self.tweet_map[uid]:
                index = len(self.tweet_map[uid]) - 1
                time, tweet_id = self.tweet_map[uid][index]
                heapq.heappush(max_heap, (-time, tweet_id, uid, index - 1))

        result = []

        while max_heap and len(result) < 10:
            time, tweet_id, uid, next_index = heapq.heappop(max_heap)
            result.append(tweet_id)

            if next_index >= 0:
                next_time, next_tweet_id = self.tweet_map[uid][next_index]
                heapq.heappush(max_heap, (-next_time, next_tweet_id, uid, next_index - 1))

        return result

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        
