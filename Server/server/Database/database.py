from server.Database.SQLite.sqlite_database import SQLite




class Database:
    def load(database, databaseType):
        databaseType = databaseType.lower()


        if databaseType == "sqlite":
            return SQLite(database)