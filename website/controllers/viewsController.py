from flask import request, render_template, jsonify, flash, redirect, url_for
from website.services.userServices import loginU



def home():
    return render_template('home.html')
