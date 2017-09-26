import os
from logging import DEBUG

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Configure DB
app.config['SECRET_KEY'] = '(\x86w\x94Cz\x99\xda\x1e^K=\x06\x9e\xc1(e\xd72\r\x9a\xc9\xc5\xc8'
app.config['DEBUG'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///thermos.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(base_dir, 'thermos.db'))
app.logger.setLevel(DEBUG)
db = SQLAlchemy(app)
db.create_all()


# Configure Authentication
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)


# Import at end to workaround recursive imports
import models
import views