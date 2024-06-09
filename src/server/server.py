import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from firebase_admin import credentials, initialize_app
from src.database.settings import db
from src.routes.users_routes import users_routes_bp
from src.routes.pets_routes import pets_routes_bp
from src.server.credentials import cred_firebase

load_dotenv()

app = Flask(__name__)
CORS(app)
migrate = Migrate()
jwt = JWTManager()

cred = credentials.Certificate(cred_firebase)
initialize_app(cred, {'storageBucket': 'petshop-7e2a6.appspot.com'})

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify({"message": "Token has expired", "error": "token_expired"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify(
                {"message": "Signature verification failed", "error": "invalid_token"}
            ),
            401,
        )
@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify(
            {
                "message": "Request doesnt contain valid token",
                "error": "authorization_header",
            }
        ),
        401,
    )

def create_app():
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['FLASK_SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    app.register_blueprint(users_routes_bp, url_prefix='/users')
    app.register_blueprint(pets_routes_bp, url_prefix='/pets')

    return app
    