from flask import request, render_template, jsonify, flash, redirect, url_for, session
from website.services.userServices import create_user, loginU
from flask_login import login_user, login_required, logout_user, current_user


def sign_up_name():
    if request.method == 'GET':
        return render_template('signup_name.html')
    elif request.method == 'POST':
        username = request.form.get('name')
        session['username'] = username
        return redirect(url_for('user_bp.signup_email'))


def signup_email():
    if request.method == 'GET':
        return render_template("signup_email.html")
    elif request.method == 'POST':
        user_email = request.form.get('email')
        session['email'] = user_email
        return redirect(url_for('user_bp.signup_password'))


def signup_password():
    if request.method == 'GET':
        return render_template('signup_password.html')
    elif request.method == 'POST':
        password = request.form.get('password')
        create_user(email=session['email'], password=password, username=session['username'])
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
        
def logout():
    logout_user()
    return redirect(url_for('views_bp.home'))






