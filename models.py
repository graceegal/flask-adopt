"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True)

    name = db.Column(
        db.String(25),
        nullable=False
    )

    species = db.Column(
        db.String(25),
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        default=''
    )

    # TODO: do we add a filter for input options here?
    age = db.Column(
        db.Text,
        nullable=False
    )

    notes = db.Column(
        db.Text,
        nullable=True
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )