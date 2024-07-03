from flask import request, render_template, jsonify, flash, redirect, url_for
from website.services.userServices import create_user, loginU


def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    elif request.method == 'POST':
        create_user(request.form)
        return redirect(url_for('views_bp.home'))

def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        log = loginU(email, password)
        if log:
            return redirect(url_for('views_bp.home'))
        else:
            return render_template("login.html")
