from flask import request, render_template, jsonify, flash, redirect, url_for
from website.services.events_services import get_events, get_searched_events
from flask_login import login_required, current_user


@login_required
def home():
    if request.method == 'GET':
        events = get_events()
        return render_template('home.html', user = current_user, events = events)
    elif request.method == 'POST':
        search = request.form.get('search')
        if search:
            events = get_searched_events(search)
            if events:
                return render_template('event_search.html', events=events)
            else:
                return render_template('no_results.html')
        else:
            return render_template('no_results.html')

def start():
    return render_template('start.html')

def landing_page():
    return render_template('landingPage.html')