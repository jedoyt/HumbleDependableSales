#PyAny_MainApp/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

########################
#### DATABASE SETUP ####
########################
# Using SQLite #
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
################

# Using MySQL #
# "None for fow"
###############

db = SQLAlchemy(app)
Migrate(app,db)
########################

#######################
#### LOGIN CONFIGS ####
#######################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
#######################

#################################
#### BLUEPRINT REGISTRATIONS ####
#################################
from PyAny_MainApp.core.views import core
app.register_blueprint(core)

from PyAny_MainApp.error_pages.handlers import error_pages
app.register_blueprint(error_pages)

from PyAny_MainApp.posts.views import blog_posts
app.register_blueprint(blog_posts)

from PyAny_MainApp.users.views import users
app.register_blueprint(users)

from PyAny_MainApp.covid19_dailyreports.views import covid19_dailyreports
app.register_blueprint(covid19_dailyreports)

from PyAny_MainApp.flames_app.views import flames_app
app.register_blueprint(flames_app)
#################################