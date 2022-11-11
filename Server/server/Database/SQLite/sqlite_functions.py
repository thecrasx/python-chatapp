import sqlite3
from typing import List




class SQLiteFunctions:
    def __init__(self, database) -> None:
        
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()



    def close(self):
        self.conn.close()



    def execute(self, command):
        try:
            self.cursor.execute(command)
            return True
        except Exception as e:
            print(e)
            return False


    def commit(self):
        self.conn.commit()


    def fetchOne(self):
        return self.cursor.fetchone()

    def fetchMany(self, size: int):
        return self.cursor.fetchmany(size)

    def fetchAll(self):
        return self.cursor.fetchall()

    def recordExist(self):
        if self.fetchOne():
            return True
        else:
            return False


    
    def isExecutedSuccessfully(self, executionSuccess, commitOnSuccess=False) -> bool:
        if executionSuccess:
                if commitOnSuccess:
                    self.commit()
                return True
        else:
            return False



    #############################################



    def isCredentialsValid(self, password, username=None, email=None) -> bool:
        if username == None and email == None:
            return False

        if username:
            self.execute(f"SELECT * FROM Users WHERE username = '{username}'")

        elif email:
            self.execute(f"SELECT * FROM Users WHERE email = '{email}'")

        
        # STRUCTURE - ( user_id, username, email, password )
        credentials = self.fetchOne()
        
        if credentials != None:
            if password == credentials[3]:
                return True

            else:
                return False

        else:
            return False



    def checkIfUsernameExists(self, username) -> bool:
        self.execute(f"SELECT * FROM Users WHERE username = '{username}'")
        
        return self.recordExist()



    def checkIfEmailExists(self, email) -> bool:
        self.execute(f"SELECT * FROM Users WHERE email = '{email}'")
        
        return self.recordExist()



    #############################################



    def addUser(self, username, email, password) -> bool:
        executionSuccess = self.execute(
            f"INSERT INTO Users (username, email, password) VALUES ('{username}', '{email}', '{password}')" )

        output = self.isExecutedSuccessfully(executionSuccess, commitOnSuccess=True)
        return output



    def deleteUser(self, username=None, email=None) -> bool:
        if username:
            executionSuccess = self.execute(f"DELETE FROM Users WHERE username = '{username}'")

        elif email:
            executionSuccess = self.execute(f"DELETE FROM Users WHERE email = '{email}'")
        
        if username != None or email != None:
            output = self.isExecutedSuccessfully(executionSuccess, commitOnSuccess=True)
            return output
        else:
            return False


    def getUserData(self, userId=None, username = None, email = None):
        if userId:
            self.execute(f"SELECT * FROM Users WHERE user_id = {userId}")
        
        elif username:
            self.execute(f"SELECT * FROM Users WHERE username = '{username}'")
        
        elif email:
            self.execute(f"SELECT * FROM Users WHERE email = '{email}'")

        
        if userId != None or username != None or email != None:
            data = self.fetchOne()

            if data:
                return {"user_id": data[0], 
                        "username": data[1], 
                        "email": data[2],
                        "profile_photo": data[4]}

            else:
                return False

        else:
            return False



    def getUsersData(self, username, amount) -> list:
        if amount <= 0:
            return []

        self.execute(f"SELECT * FROM Users WHERE username LIKE '{username}%'")

        users = self.fetchMany(amount)
        #print(f"DB: {users}")
        usersData = []

        for user in users:
            usersData.append({"user_id": user[0], 
                            "username": user[1], 
                            "email": user[2],
                            "profile_photo": user[4]})

        return usersData




    #############################################



    def changeUsername(self, oldUsername, newUsername) -> bool:
        executionSuccess = self.execute(f"UPDATE Users SET username = '{newUsername}' WHERE username IS '{oldUsername}'")
        
        output = self.isExecutedSuccessfully(executionSuccess, commitOnSuccess=True)
        return output



    def changeEmail(self, oldEmail, newEmail) -> bool:
        executionSuccess = self.execute(f"UPDATE Users SET email = '{newEmail}' WHERE email IS '{oldEmail}'")
        
        output = self.isExecutedSuccessfully(executionSuccess, commitOnSuccess=True)
        return output



    def changePassword(self, newPassword, username=None, email=None) -> bool:
        if username:
            executionSuccess = self.execute(f"UPDATE Users SET password = '{newPassword}' WHERE username IS '{username}'")

        elif email:
            executionSuccess = self.execute(f"UPDATE Users SET password = '{newPassword}' WHERE email IS '{email}'")

        if username != None or email != None:
            output = self.isExecutedSuccessfully(executionSuccess, commitOnSuccess=True)
            return output
        else:
            return False


    def changeProfilePhoto(self, photo, username = None, email = None):
        
        if username:
            executionSuccess = self.execute(f"UPDATE Users SET profile_photo = '{photo}' WHERE username IS '{username}'")

        elif email:
            executionSuccess = self.execute(f"UPDATE Users SET profile_photo = '{photo}' WHERE email IS '{email}'")

        if username != None or email != None:
            output = self.isExecutedSuccessfully(executionSuccess, commitOnSuccess=True)
            return output
        else:
            return False



    #############################################

    def checkIfUserExists(self, userId):
        self.execute(f"SELECT user_id FROM Users WHERE user_id = {userId}")

        return self.recordExist()

    def checkIfRequestExists(self, userId, friendId):
        self.execute(f"SELECT * FROM UserRequests WHERE user_id = {userId} AND friend_id = {friendId}")

        if not self.recordExist():
            self.execute(f"SELECT * FROM FriendRequests WHERE user_id = {userId} AND friend_id = {friendId}")

            if self.recordExist():
                return True
            else:
                return False

        else:
            return True

    def isFriends(self, userId, friendId):
        self.execute(f"SELECT * FROM Friends WHERE user_id = {userId} AND friend_id = {friendId}")
        return self.recordExist()


    def removeFriend(self, userId, friendId):
        if self.isFriends(userId, friendId):
            self.execute(f"DELETE FROM Friends WHERE user_id = {userId} AND friend_id = {friendId}")
            self.execute(f"DELETE FROM Friends WHERE user_id = {friendId} AND friend_id = {userId}")
            self.commit()

        if not self.isFriends(userId, friendId):
            return True
        else:
            return False


    def getFriends(self, userId):
        self.execute(f"SELECT friend_id FROM Friends WHERE user_id = {userId}")
        data = self.fetchAll()
        friends = []
        print(data)

        if data:
            for friendId in data:
                friends.append(self.getUserData(friendId[0]))

        return friends


    def deleteFriendRequest(self, userId, friendId):
        self.execute(f"DELETE FROM UserRequests WHERE user_id = {userId} AND friend_id = {friendId}")
        self.execute(f"DELETE FROM FriendRequests WHERE user_id = {friendId} AND friend_id = {userId}")
        self.commit()

        if not self.checkIfRequestExists(userId, friendId):
            return True
        else:
            return False


    def cancelFriendRequest(self, userId, friendId):
        return self.deleteFriendRequest(userId, friendId)


    def sendFriendRequest(self, userId, friendId):
        if userId == friendId or self.isFriends(userId, friendId):
            return False
        
        if self.checkIfRequestExists(userId, friendId):
            return False

        self.execute(f"INSERT INTO UserRequests (user_id, friend_id) VALUES ({userId}, {friendId})")
        self.execute(f"INSERT INTO FriendRequests (user_id, friend_id) VALUES ({friendId}, {userId})")
        self.commit()

        if self.checkIfRequestExists(userId, friendId):
            return True
        else:
            return False


    def getFriendRequests(self, userId):
        self.execute(f"SELECT friend_id FROM FriendRequests WHERE user_id = {userId}")

        data = self.fetchAll()

        if data:
            friendsData = []

            for friendId in data:
                friend = self.getUserData(friendId)
                
                if friend:
                    friendsData.append(friend)


            return friendsData

        else:
            return None


    def getUserRequests(self, userId):
        self.execute(f"SELECT friend_id FROM UserRequests WHERE user_id = {userId}")

        data = self.fetchAll()

        if data:
            return data
        else:
            return None


    def acceptFriendRequest(self, userId, friendId):
        if not self.checkIfRequestExists(userId, friendId):
            return False

        self.deleteFriendRequest(userId, friendId)
        self.execute(f"INSERT INTO Friends (user_id, friend_id) VALUES ({userId}, {friendId})")
        self.execute(f"INSERT INTO Friends (user_id, friend_id) VALUES ({friendId}, {userId})")
        self.commit()

        return self.isFriends(userId, friendId)


    def declineFriendRequest(self, userId, friendId):
        if not self.checkIfRequestExists(userId, friendId):
            return False


        if self.deleteFriendRequest(friendId, userId):
            return True
        else:
            return False

    
    def findNewFriends(self, userId, username, amount):
        users = self.getUsersData(username, amount)
        newFriends = []

        if not users:
            return []

        for user in users:
            friendId = user["user_id"]
            
            if userId == friendId:
                pass

            else:
                if self.isFriends(userId, friendId):
                    pass

                else:
                    if self.checkIfRequestExists(friendId, userId):
                        pass
                    
                    else:
                        if self.checkIfRequestExists(userId, friendId):
                            user["user_request"] = 1
                        else:
                            user["user_request"] = 0

                        newFriends.append(user)

        
        return newFriends
        

    
    #############################################


