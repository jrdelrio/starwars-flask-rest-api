"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# @app.route('/user', methods=['GET'])
# def handle_hello():
#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }
#     return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = [planet.serialize_all() for planet in Planet.query.all()]
    print(Planet.query.all())
    response_body = {
        "msg": "Hello, this is your GET /planets response.",
        "results": planets
    }
    return jsonify(response_body), 200

@app.route('/planet/<int:id_planet>', methods=['GET'])
def get_planet(id_planet):
    planet = Planet.query.get(id_planet)
    response_body = {
        "msg": "Hello, this is your GET /planets response.",
        "results": planet.serialize()
    }
    return jsonify(response_body), 200

@app.route('/characters', methods=['GET'])
def get_characters():
    characters = [character.serialize_all() for character in Character.query.all()]
    response_body = {
        "msg": "Hello, this is your GET /characters response.",
        "results": characters
    }
    return jsonify(response_body), 200

@app.route('/character/<int:id_character>', methods=['GET'])
def get_character(id_character):
    character = Character.query.get(id_character)
    response_body = {
        "msg": "Hello, this is your GET /planets response.",
        "results": character.serialize()
    }
    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
