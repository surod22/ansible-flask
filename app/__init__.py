from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CsrfProtect

csrf = CsrfProtect()
app = Flask(__name__)
csrf.init_app(app)
app.config.from_object('config')
app.secret_key = 'ansible key'



db = SQLAlchemy(app)

from app import views, models
