from flask import Flask
from .config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pyttsx3
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

socketio = SocketIO(app, cors_allowed_origins='*')
socketio.run(app)
CORS(app)


from app import views