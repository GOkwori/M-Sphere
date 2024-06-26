import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


db = SQLAlchemy(app)
migrate = Migrate(app, db)
    

def create_app():
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    from m_sphere import routes
    return app



