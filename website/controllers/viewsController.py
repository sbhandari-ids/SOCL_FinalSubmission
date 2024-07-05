from flask import request, render_template, jsonify, flash, redirect, url_for
from website.services.events_services import get_events
from flask_login import login_required, current_user


@login_required
def home():
    events = get_events()
    return render_template('eventsHome.html', user = current_user, events = events)

def main():
    return render_template('signInSignUp4.html')
