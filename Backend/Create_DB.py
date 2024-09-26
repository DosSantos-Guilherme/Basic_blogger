import sqlite3

dataBaseConnection = sqlite3.connect('DummyDatabase.db')
dataBase = dataBaseConnection.cursor()

dataBase.execute("""
    CREATE TABLE IF NOT EXISTS User (
                 UserID INTEGER PRIMARY KEY,
                 Username TEXT NOT NULL,
                 Password TEXT NOT NULL,
                 Role TEXT NOT NULL
                 )
""")

dataBase.execute("""
    CREATE TABLE IF NOT EXISTS Student (
        UserID INTEGER PRIMARY KEY,
        GradeLevel TEXT,
        FOREIGN KEY(UserID) REFERENCES User(UserID)
        )
""")

dataBase.execute("""
    CREATE TABLE IF NOT EXISTS Teacher (
        UserID INTEGER PRIMARY KEY,
        Subject TEXT,
        FOREIGN KEY(UserID) REFERENCES User(UserID)
        )
""")
dataBase.execute("""
    CREATE TABLE IF NOT EXISTS BlogPost (
        PostID INTEGER PRIMARY KEY,
        Title TEXT NOT NULL,
        Content TEXT NOT NULL,
        UserID INTEGER,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(UserID) REFERENCES User(UserID)
    )
""")

# Create Comment table
dataBase.execute("""
    CREATE TABLE IF NOT EXISTS Comment (
        CommentID INTEGER PRIMARY KEY,
        Content TEXT NOT NULL,
        PostID INTEGER,
        UserID INTEGER,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(PostID) REFERENCES BlogPost(PostID),
        FOREIGN KEY(UserID) REFERENCES User(UserID)
    )
""")

# Create Progress table
dataBase.execute("""
    CREATE TABLE IF NOT EXISTS Progress (
        ProgressID INTEGER PRIMARY KEY,
        UserID INTEGER,
        PostID INTEGER,
        Feedback TEXT,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(UserID) REFERENCES User(UserID),
        FOREIGN KEY(PostID) REFERENCES BlogPost(PostID)
    )
""")

# Commit the changes and close the connection
dataBaseConnection.commit()
dataBaseConnection.close()
