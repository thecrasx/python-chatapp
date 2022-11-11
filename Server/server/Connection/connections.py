




class ConnectionData:
    def __init__(self, client, address):
        self.client = client
        self.address = address



class Connections:
    def __init__(self):
        self.data = {}  # { "userId": { "socket" : socket,
                        #                 "address": ( ip, port ) }}


      
    def add(self, userId, socket, address):
        self.data[userId] = { "socket": socket,
                                "address": address }



    def get(self, userId):
        data = self.data.get(userId)

        if data:
            return ConnectionData(data["socket"], data["address"])
        else:
            return None


    
    def close(self, userId=None, socket=None, address=None) -> None:

        if userId:
            if self.is_connected(userId):
                self.data.pop(userId)

        elif socket:
            for key in self.data:
                if self.data[key]["socket"] == socket:
                    self.data.pop(key)
                    break

        elif address:
            for key in self.data:
                if self.data[key]["address"] == address:
                    self.data.pop(key)
                    break


          
    def isConnected(self, userId=None, socket=None, address=None) -> bool:
        if userId:      
            if userId in self.data:
                return True
            else:
                return False

        elif socket:
            for key in self.data:
                if self.data[key]["socket"] == socket:
                    return True

        elif address:
            for key in self.data:
                if self.data[key]["address"] == address:
                    return True

            return False