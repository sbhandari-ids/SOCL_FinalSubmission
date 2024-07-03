from flask import request, render_template, jsonify, flash, redirect, url_for
from website.services.userServices import loginU
from flask_login import login_required


@login_required
def home():
    return render_template('home.html')
