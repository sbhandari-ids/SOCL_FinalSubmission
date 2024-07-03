from flask import Blueprint
from website.controllers.viewsController import home

views_blueprint = Blueprint("views_bp", __name__)


views_blueprint.route('/', methods=['GET'])(home)