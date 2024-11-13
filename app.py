from flask import Flask, make_response, request, jsonify, Blueprint
from flask_migrate import Migrate
from models import *
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required
from flask_cors import CORS
from dotenv import load_dotenv
import os
from blueprints.auth import auth_blueprint

load_dotenv()

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY")

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
CORS(app)

# @app.route("/", methods=["GET"])
# def index():
#     return {"message": "Debugging"}

app.register_blueprint(auth_blueprint)


if __name__ == "__main__":
    app.run(port=8081, debug=True)
