from flask import Flask
from website.schemas import ma
from flask_sqlalchemy import SQLAlchemy
from os import path
from website.database import db
from flask_login import LoginManager

from website.routes.viewsBP import views_blueprint
from website.routes.userBP import user_blueprint


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Hello World'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:A6d0a6m1!@localhost/socl'
    db.init_app(app)
    # login_manager = LoginManager()
    # login_manager.init_app(app)


    app.register_blueprint(views_blueprint, url_prefix='/')
    app.register_blueprint(user_blueprint, url_prefix='/')

    from website.models import user

    with app.app_context():
        db.drop_all()
        db.create_all()    

    return app




