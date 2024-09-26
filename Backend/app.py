from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__,template_folder='../Frontend/Pages',static_folder='../Frontend/static')

# Configure the SQLite database using the absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////root/Documents/GS_blog/Backend/DummyDatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    __tablename__ = 'User'
    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String, nullable=False)
    Password = db.Column(db.String, nullable=False)
    Role = db.Column(db.String, nullable=False)

# Define the Student model
class Student(db.Model):
    __tablename__ = 'Student'
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'), primary_key=True)
    GradeLevel = db.Column(db.String)

# Define the Teacher model
class Teacher(db.Model):
    __tablename__ = 'Teacher'
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'), primary_key=True)
    Subject = db.Column(db.String)

# Define the BlogPost model
class BlogPost(db.Model):
    __tablename__ = 'BlogPost'
    PostID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String, nullable=False)
    Content = db.Column(db.String, nullable=False)
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))
    CreatedAt = db.Column(db.DateTime, default=db.func.current_timestamp())

# Define the Comment model
class Comment(db.Model):
    __tablename__ = 'Comment'
    CommentID = db.Column(db.Integer, primary_key=True)
    Content = db.Column(db.String, nullable=False)
    PostID = db.Column(db.Integer, db.ForeignKey('BlogPost.PostID'))
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))
    CreatedAt = db.Column(db.DateTime, default=db.func.current_timestamp())

# Define the Progress model
class Progress(db.Model):
    __tablename__ = 'Progress'
    ProgressID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))
    PostID = db.Column(db.Integer, db.ForeignKey('BlogPost.PostID'))
    Feedback = db.Column(db.String)
    CreatedAt = db.Column(db.DateTime, default=db.func.current_timestamp())

# Create the database and tables
with app.app_context():
    db.create_all()

# Serve the HTML file
@app.route('/')
def index():
    return render_template('index.html')

# POST method to register a new user
@app.route('/api/register', methods=['POST'])
def register():
    user_data = request.get_json()
    new_user = User(Username=user_data['username'], Password=user_data['password'], Role=user_data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# GET method to retrieve user profile
@app.route('/api/profile/<username>', methods=['GET'])
def get_profile(username):
    user = User.query.filter_by(Username=username).first()
    if user:
        return jsonify({"username": user.Username, "role": user.Role})
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
