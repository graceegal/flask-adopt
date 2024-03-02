"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def show_homepage():
    """Show homepage which lists the pets"""
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """ Pet add form; handle adding. """

    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(
        name = form.name.data,
        species = form.species.data,
        photo_url = form.photo_url.data or None,
        age = form.age.data,
        notes = form.notes.data
        )

        db.session.add(new_pet)
        db.session.commit()

        # flash(f'Added {name}')
        return redirect("/")

    else:
        return render_template(
            "pet_add_form.html", form=form
        )

@app.get('/<int: pet_id>')
def show_pet_page(pet_id):
    """Show pet page"""
    pet = Pet().query.get_or_404(pet_id)
    return render_template('pet_page.html', pet=pet)



