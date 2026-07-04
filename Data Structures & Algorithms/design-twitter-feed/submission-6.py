class Twitter:

    def __init__(self):
        self.user_follower = {} ## {userID: {followerID1, followerID2}}
        self.user_tweet = {} ## {userID:[[tweet_id1, count0],]}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId in self.user_tweet:
            self.user_tweet[userId].append([-1*self.time, tweetId])
        else:
            self.user_tweet[userId] = [[-1*self.time, tweetId]]

        if not userId in self.user_follower:
            self.user_follower[userId] = set()
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        res = []
        followers = self.user_follower[userId]
        
        tweets = self.user_tweet[userId].copy()
        for f in followers:
            tweets.extend(self.user_tweet[f])
        heapq.heapify(tweets)
        
        count = 0
        while len(tweets) > 0 and count < 10:
            time, _id = heapq.heappop(tweets)
            res.append(_id)
            count += 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        if not followerId in self.user_tweet:
            self.user_tweet[followerId] = []
        if not followeeId in self.user_tweet:
            self.user_tweet[followeeId] = []

        if followerId in self.user_follower:
            self.user_follower[followerId].add(followeeId)
        else:
            self.user_follower[followerId] = set([followeeId])


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if (followerId in self.user_follower) and (followeeId in self.user_follower[followerId]):
            self.user_follower[followerId].remove(followeeId)
