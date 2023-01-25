from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(50))
    terrain = db.Column(db.String(50))
    diameter = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    url = db.Column(db.String(100), unique=True)

    def serialize_all(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url
        }

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "diameter": self.diameter,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "url": self.url
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    gender = db.Column(db.String(15))
    height_cm = db.Column(db.Integer)
    mass_kg = db.Column(db.Integer)
    eye_color = db.Column(db.String(20))
    hair_color = db.Column(db.String(20))
    skin_color = db.Column(db.String(20))
    url = db.Column(db.String(100), unique=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    #planet = relationship(db.Planet)
    #vehicle = relationship(db.Vehicle)

    def serialize_all(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
        }

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "height_cm": self.height_cm,
            "mass_kg": self.mass_kg,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "planet_id": self.planet_id,
            #"vehicle_id": self.vehicle_id,
            "url": self.url
        }
    
    def serialize_all(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    charac_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)