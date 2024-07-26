import googlemaps

from flask import Flask
from website.schemas import ma
from flask_sqlalchemy import SQLAlchemy
from os import path
from website.database import db
from flask_login import LoginManager
from flask_migrate import Migrate


from website.routes.viewsBP import views_blueprint
from website.routes.userBP import user_blueprint
from website.routes.eventBP import event_blueprint

# API = open('maps_key.txt', 'r')
# APIKey = API.read()

# Maps = googlemaps.Client(key = APIKey)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Hello World'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Admin123@localhost/socl'

    #elephantSQL databaseConnection.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bbzrbxtf:LhLsrlIEoxouSWnvGo4uare7rE50Ld3r@raja.db.elephantsql.com/bbzrbxtf'

    #Internal Database URL provided by Render
    # app.config['SQLALCHEMY_DATABASE_URI']='postgresql://root:Yjn200d13v2fZYDBkWAWLf30Jc573Ipn@dpg-cqhj9408fa8c73bt4el0-a/db_socl'
    #External database URL provided by Render
    # app.config['SQLALCHEMY_DATABASE_URI']='postgresql://root:Yjn200d13v2fZYDBkWAWLf30Jc573Ipn@dpg-cqhj9408fa8c73bt4el0-a.virginia-postgres.render.com/db_socl'
    db.init_app(app)



    app.register_blueprint(views_blueprint, url_prefix='/')
    app.register_blueprint(user_blueprint, url_prefix='/')
    app.register_blueprint(event_blueprint, url_prefix='/event')

    from website.models.user import User

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'views_bp.landing_page'
    migrate = Migrate(app, db)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    with app.app_context():
        # db.drop_all()
        db.create_all()    

    return app



