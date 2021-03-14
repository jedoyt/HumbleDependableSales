# models.py
from PyAny_MainApp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

class User(db.Model,UserMixin):
  __tablename__ = 'users'
  id = db.Column(db.Integer,
                 primary_key=True)
  profile_image = db.Column(db.String(72),
                            nullable=False,
                            default='default_profile.png')
  email = db.Column(db.String(64),
                    unique=True,
                    index=True)
  username = db.Column(db.String(64),
                       unique=True,
                       index=True)
  password_hash = db.Column(db.String(128))

  posts = db.relationship('BlogPost',
                          backref='author',
                          lazy=True)
  
  def __init__(self,email,username,password):
    self.email = email
    self.username = username
    self.password_hash = generate_password_hash(password)

  def check_password(self,password):
    return check_password_hash(self.password_hash,password)

  def __repr__(self):
    return f"Email: {self.email} | Username: {self.username}"

class BlogPost(db.Model):
  __tablename__ = 'blogposts'
  users = db.relationship('User')
  id = db.Column(db.Integer,
                 primary_key=True)
  user_id = db.Column(db.Integer,
                      db.ForeignKey('users.id'),nullable=False)
  timestamp = db.Column(db.DateTime,
                   nullable=False
                   )
  title = db.Column(db.String(140),
                    nullable=False,
                    default='')
  text = db.Column(db.Text,nullable=False)

  #profile_src= db.Column(db.String(128),
  #                       db.ForeignKey('users.profile_image'),nullable=False,
  #                       default="{{ url_for('static',filename='profile_pics/'+'default_profile.png') }}"
  #                       )

  def __init__(self,title,text,user_id,timestamp):
    self.title = title
    self.text = text
    self.user_id = user_id
    self.timestamp = timestamp

  def __repr__(self):
    return f"Title: {self.title} | User ID: {self.user_id} : Timestamp: {self.timestamp}"