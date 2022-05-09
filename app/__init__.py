## Imports

from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.markdown import Markdown
from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, TextAreaField, PasswordField, SelectField
from wtforms_components import ColorField
from wtforms.validators import InputRequired, DataRequired

app = Flask(__name__)

Markdown(app)
app.config["SECRET_KEY"] = "fungus"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
from app import routes