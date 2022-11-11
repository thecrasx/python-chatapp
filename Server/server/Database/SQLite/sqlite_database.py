
from venv import create
from server.path_loader import PathLoader
from server.Database.SQLite.sqlite_database_schema import *
from server.Database.SQLite.sqlite_functions import SQLiteFunctions







class SQLite(SQLiteFunctions):
    def __init__(self, database):
        if database[-3:] != ".db":
            database += ".db"

        if not '/' in database and not '\\' in database:
            # If database contains '/' or '\' it means that
            # user has entered full path to the database

            path = PathLoader("Database").getPath()
            database = path + database

        
        super().__init__(database)



        
        
    
    



if __name__ == "__main__":
    sql = SQLite("test")


    def createTables():
        tableList = [Users, Friends, UserRequests,  FriendRequests, DirectMessages, UserBlockList]
        
        for table in tableList:
            sql.execute(table)


    def printUsers(name):
        users = sql.getUsersData(f"{name}", 10)

        print([user["username"] for user in users])

    print(sql.getFriends(1))



    