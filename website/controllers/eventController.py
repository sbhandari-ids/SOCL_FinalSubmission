from flask import request, render_template, jsonify, flash, redirect, url_for, session
from website.services.events_services import get_event_by_id



def view_event(id):
    event = get_event_by_id(id)
    print(event)
    string = '<h1>' + event.event_name + '</h1>'
    return string

def upcoming_events():
    return '<h1>Upcoming events</h1>'

def nearby_events():
    return '<h1>Nearby events</h1>'

def nightclub_events():
    return '<h1>Nightclubs</h1>'

def free_events():
    return '<h1>Free events</h1>'
