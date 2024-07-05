from flask import Blueprint
from website.controllers.viewsController import home, main

views_blueprint = Blueprint("views_bp", __name__)


views_blueprint.route('/', methods=['GET'])(home)
views_blueprint.route('/main', methods=['GET'])(main)