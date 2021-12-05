import os

from flask import Flask
from flask_migrate import Migrate
from flask_uuid import FlaskUUID
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('instance/config.py', silent=True)

db = SQLAlchemy(app)
db.create_all()

flask_uuid = FlaskUUID()
flask_uuid.init_app(app)

migrate = Migrate(app, db)

from api_wordbox import api