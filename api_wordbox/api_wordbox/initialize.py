from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)

app.config.from_object('instance.config.config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from api_wordbox import api