from flask import Blueprint
from website.controllers.userController import signup_email, login, logout, signup_password

user_blueprint = Blueprint("user_bp", __name__)


user_blueprint.route('/sign-up', methods=['POST','GET'])(signup_email)
user_blueprint.route('/sign-up/<username>', methods=['POST','GET'])(signup_password)
user_blueprint.route('/login', methods=['GET', 'POST'])(login)
user_blueprint.route('/logout', methods=['GET'])(logout)

