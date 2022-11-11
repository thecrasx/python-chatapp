from client.Window.UI.Elements.UI.friends_ui import FriendUI







class Friends:
    def __init__(self, mainWindow):
        self.window = mainWindow
        self.ui = self.window.ui
        self.signals = self.window.signals

        self.friendList = []
        self.__addFriendsListed = []
        self.__friendRequestsListed = []


        # SIGNALS 
        self.signals.friendsSignal.searchNoInput.connect(self.__onSearchNoInput)
        self.signals.responseSignal.newFriends.connect(self.addFriendsList)
        self.signals.responseSignal.newFriendRequest.connect(self.loadFriendRequest)
        self.signals.responseSignal.friendRequestCanceled.connect(self.__onFriendRequestCanceled)
        self.signals.responseSignal.friendRequestAccepted.connect(self.__onFriendRequestAccepted)
        self.signals.responseSignal.friendRequestDeclined.connect(self.__onFriendRequestDeclined)
        self.signals.responseSignal.friends.connect(self.loadFriends)




    def __onSearchNoInput(self):
        if self.ui.addFriendsPage.isVisible():
            for friend in self.__addFriendsListed:
                friend.close()

            self.__addFriendsListed = []



    def loadFriends(self, friends):
        print("Friends")
        usernames = [friend.userName for friend in self.friendList]

        for friend in friends:
            if not friend["username"] in usernames:
                friend = FriendUI(self.window,
                                    friendId=friend["user_id"], 
                                    userName=friend["username"],
                                    userPhoto=friend["profile_photo"])

                self.friendList.append(friend)
    
    
    
    def addFriendsList(self, users):
        if users:
            usernames = [user["username"] for user in users]
            listedFriendsUsername = []
            listedFriends = []

            # Close all users from the'__addFriendsListed' that are not in the 'users'
            for friend in self.__addFriendsListed:
                if not friend.userName in usernames:
                    friend.close()
                else:
                    listedFriends.append(friend)
                    listedFriendsUsername.append(friend.userName)

            
            for user in users:
                username = user["username"]

                if not username in listedFriendsUsername:
                    friend = FriendUI(self.window,
                                    friendId=user["user_id"], 
                                    userName=user["username"],
                                    userPhoto=user["profile_photo"], 
                                    add=True,
                                    requestSent=user["user_request"])

                    listedFriends.append(friend)

            self.__addFriendsListed = listedFriends
        
        else:
            for friend in self.__addFriendsListed:
                friend.close()

            self.__addFriendsListed = []


    def loadFriendRequest(self, friend):
        if friend:
            friend = FriendUI(self.window,
                                friendId=friend["user_id"], 
                                userName=friend["username"],
                                userPhoto=friend["profile_photo"], 
                                request=True )

            self.__friendRequestsListed.append(friend)


    
    def loadFriendRequests(self, friends):
        if friends:
            for friend in friends:
                friend = FriendUI(self.window,
                                friendId=friend["user_id"], 
                                userName=friend["username"],
                                userPhoto=friend["profile_photo"], 
                                request=True )

            self.__friendRequestsListed.append(friend)


    def removeFriendFromFriendRequests(self, friendId) -> list:
        friendData = []

        for friend in self.__friendRequestsListed:
            if friend.friendId == friendId:
                self.__friendRequestsListed.remove(friend)

                friendData.append(friend.friendId)
                friendData.append(friend.userName)
                friendData.append(friend.userPhoto)
                friend.close()
                del friend

        return friendData


    def __onFriendRequestCanceled(self, friendId):
        self.removeFriendFromFriendRequests(friendId)
            

    def __onFriendRequestDeclined(self, friendId):
        print(f"FriendId: {friendId}")
        self.removeFriendFromFriendRequests(friendId)


    def __onFriendRequestAccepted(self, friendData):
        if type(friendData) is int:
            friendData = self.removeFriendFromFriendRequests(friendData)

            if friendData:
                friend = FriendUI(self.window,
                                    friendId=friendData[0], 
                                    userName=friendData[1],
                                    userPhoto=friendData[2] )

                self.friendList.append(friend)
        
        else:
            friend = FriendUI(self.window,
                                friendId=friend["user_id"], 
                                userName=friend["username"],
                                userPhoto=friend["profile_photo"] )
            
            self.friendList.append(friend)