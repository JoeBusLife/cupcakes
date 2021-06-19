"""Flask app for Cupcakes"""
from flask import Flask, request, render_template, jsonify, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Cupcake
from forms import CupcakeForm
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "soup"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()



@app.route('/')
def index_page():
    """Renders html template that includes some JS - NOT PART OF JSON API!"""
    form = CupcakeForm()
    return render_template('index.html', form=form)


# *****************************
# RESTFUL CUPCAKES JSON API
# *****************************
@app.route('/api/cupcakes')
def list_cupcakes():
    """Returns JSON w/ all cupcakes"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes/<int:cup_id>')
def get_cupcake(cup_id):
    """Returns JSON for one cupcake in particular"""
    cupcake = Cupcake.query.get_or_404(cup_id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Creates a new cupcake and returns JSON of that created cupcake"""
    new_cupcake = Cupcake(flavor=request.json['flavor'],
                            rating=request.json['rating'],
                            size=request.json['size'],
                            image=request.json['image'] or None)
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)


@app.route('/api/cupcakes/<int:cup_id>', methods=["PATCH"])
def update_cupcake(cup_id):
    """Updates a particular cupcake and responds w/ JSON of that updated cupcake"""
    cupcake = Cupcake.query.get_or_404(cup_id)
    
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size',  cupcake.size)
    cupcake.rating = request.json.get('rating',  cupcake.rating)
    cupcake.image = request.json.get('image',  cupcake.image)
    db.session.commit()
    
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:cup_id>', methods=["DELETE"])
def delete_cupcake(cup_id):
    """Deletes a particular cupcake"""
    cupcake = Cupcake.query.get_or_404(cup_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")