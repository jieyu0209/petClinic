from flask import Flask
#from pet.config import Config
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object(Config)
#db = SQLAlchemy(app)

from pet import routes



