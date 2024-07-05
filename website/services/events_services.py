from website.models.event import Event
from flask import flash, redirect, url_for
from website.database import db

def get_events():
    events = []
    for i in range(1,7):
        events.append(Event.query.filter_by(id=i).first())
    return events
