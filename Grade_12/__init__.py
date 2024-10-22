from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)
app.config["SECRET_KEY"] = "do not try"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

#create database 
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"


from Grade_12 import views
from Grade_12 import models

if __name__ == "__main__": 
    app.run(debug=True)