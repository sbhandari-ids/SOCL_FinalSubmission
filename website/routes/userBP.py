from flask import Blueprint
from website.controllers.userController import signup, login

user_blueprint = Blueprint("user_bp", __name__)


user_blueprint.route('/sign-up', methods=['POST','GET'])(signup)
user_blueprint.route('/login', methods=['GET', 'POST'])(login)
