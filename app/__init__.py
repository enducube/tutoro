## Imports

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.markdown import Markdown
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

app = Flask(__name__)
Markdown(app)
app.config["SECRET_KEY"] = "fungus"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from app import routes