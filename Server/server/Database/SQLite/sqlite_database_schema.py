



################### Tables ###################

Users = '''CREATE TABLE IF NOT EXISTS Users ( 
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT NOT NULL,
    profile_photo TEXT
    )'''


Friends = '''CREATE TABLE IF NOT EXISTS Friends (
    user_id INTEGER,
    friend_id INTEGER,

    FOREIGN KEY ( user_id )
        REFERENCES Users ( user_id ),

    FOREIGN KEY ( friend_id )
        REFERENCES Users ( user_id )
)'''

UserRequests = '''CREATE TABLE IF NOT EXISTS UserRequests (
    user_id INTEGER,
    friend_id INTEGER,

    FOREIGN KEY ( user_id )
        REFERENCES Users ( user_id ),

    FOREIGN KEY ( friend_id )
        REFERENCES Users ( user_id )
)'''


FriendRequests = '''CREATE TABLE IF NOT EXISTS FriendRequests (
    user_id INTEGER,
    friend_id INTEGER,

    FOREIGN KEY ( user_id )
        REFERENCES Users ( user_id ),

    FOREIGN KEY ( friend_id )
        REFERENCES Users ( user_id )
)'''


DirectMessages = '''CREATE TABLE IF NOT EXISTS DirectMessages (
    user_id INTEGER NOT NULL,
    sender_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    date_time DATETIME NOT NULL,

    FOREIGN KEY ( user_id )
        REFERENCES Users ( user_id ),

    FOREIGN KEY ( sender_id )
        REFERENCES Users ( user_id )
)'''


UserBlockList = '''CREATE TABLE IF NOT EXISTS UserBlockList (
    user_id INTEGER NOT NULL,
    blocked_user_id INTEGER NOT NULL,

    FOREIGN KEY ( user_id )
        REFERENCES Users ( user_id ),

    FOREIGN KEY ( blocked_user_id )
        REFERENCES Users ( user_id )
)'''