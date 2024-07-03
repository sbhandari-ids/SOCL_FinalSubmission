import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


MIGRATIONS_FOLDER = os.environ.get('MIGRATIONS_FOLDER') or 'migrations'


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

