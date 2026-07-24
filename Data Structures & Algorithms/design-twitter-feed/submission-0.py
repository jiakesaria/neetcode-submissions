class Twitter:
    #hashmap with key as userid and value as a list of tweets under that userid
    def __init__(self):
        self.count = 0
        self.tweetList = defaultdict(list) 
        self.followerList = defaultdict(set)   

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetList[userId].append([self.count, tweetId]) #latest tweets appended last
        self.count -= 1 #supports minheap 

    def getNewsFeed(self, userId: int) -> List[int]:
        #heap grab top 10 for each grabbed tweet check in folloerlist but if i pop it cant be used for next.....! 
        res = []
        minHeap = []
        self.followerList[userId].add(userId)
        for followee in self.followerList[userId]: 
            if followee in self.tweetList:
                index = len(self.tweetList[followee]) - 1 #latest tweet

                time, tweetid = self.tweetList[followee][index]

                heapq.heappush(minHeap, [time, tweetid, followee, index - 1])
        #minHeap has the latest tweet of each followee
        while minHeap and len(res) < 10:
            time, tweetid, followee, index = heapq.heappop(minHeap)
            res.append(tweetid)
            if index >= 0:
                time, tweetid = self.tweetList[followee][index]
                heapq.heappush(minHeap, [time, tweetid, followee, index - 1])

        return res
    

    def follow(self, followerId: int, followeeId: int) -> None:
        #create a hashmap where key is follower and has a list of followerIds 
        #append followee      
        self.followerList[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerList[followerId]:
            self.followerList[followerId].remove(followeeId)
