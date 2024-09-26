import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('DummyDatabase.db')
c = conn.cursor()

# Insert users (3 students and 1 teacher)
users = [
    ('student1', 'password123', 'Student'),
    ('student2', 'password123', 'Student'),
    ('student3', 'password123', 'Student'),
    ('teacher1', 'password123', 'Teacher')
]
c.executemany('INSERT INTO User (Username, Password, Role) VALUES (?, ?, ?)', users)

# Get user IDs
c.execute('SELECT UserID FROM User WHERE Role = "Student"')
student_ids = [row[0] for row in c.fetchall()]
c.execute('SELECT UserID FROM User WHERE Role = "Teacher"')
teacher_id = c.fetchone()[0]

# Insert students and teacher details
students = [(student_ids[0], 'Grade 10'), (student_ids[1], 'Grade 11'), (student_ids[2], 'Grade 12')]
teacher = (teacher_id, 'Mathematics')
c.executemany('INSERT INTO Student (UserID, GradeLevel) VALUES (?, ?)', students)
c.execute('INSERT INTO Teacher (UserID, Subject) VALUES (?, ?)', teacher)

# Insert blog posts
blog_posts = [
    ('First Blog Post', 'This is the content of the first blog post.', student_ids[0]),
    ('Second Blog Post', 'This is the content of the second blog post.', student_ids[1])
]
c.executemany('INSERT INTO BlogPost (Title, Content, UserID) VALUES (?, ?, ?)', blog_posts)

# Get blog post IDs
c.execute('SELECT PostID FROM BlogPost')
post_ids = [row[0] for row in c.fetchall()]

# Insert comments
comments = [
    ('Great post!', post_ids[0], student_ids[1]),
    ('Very informative.', post_ids[0], student_ids[2]),
    ('Thanks for sharing!', post_ids[0], teacher_id),
    ('Nice work!', post_ids[1], student_ids[0]),
    ('I learned a lot.', post_ids[1], student_ids[2]),
    ('Well written!', post_ids[1], teacher_id),
    ('Interesting read.', post_ids[0], student_ids[0]),
    ('Good job!', post_ids[1], student_ids[1]),
    ('Helpful post.', post_ids[0], student_ids[2]),
    ('Keep it up!', post_ids[1], teacher_id)
]
c.executemany('INSERT INTO Comment (Content, PostID, UserID) VALUES (?, ?, ?)', comments)

# Insert progress
progress = [
    (student_ids[0], post_ids[0], 'Good start, keep improving.'),
    (student_ids[1], post_ids[1], 'Well done, try to add more details.'),
    (student_ids[2], post_ids[0], 'Great effort, focus on clarity.'),
    (student_ids[0], post_ids[1], 'Nice post, work on your grammar.'),
    (student_ids[1], post_ids[0], 'Good content, add more examples.')
]
c.executemany('INSERT INTO Progress (UserID, PostID, Feedback) VALUES (?, ?, ?)', progress)

# Commit the changes and close the connection
conn.commit()
conn.close()
