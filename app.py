from flask import Flask, make_response, request, jsonify, Blueprint
from flask_migrate import Migrate
from models import *
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
import os
from blueprints.auth import auth_blueprint
from blueprints.blogs_blueprint import blogs_bp
from blueprints.comments_blueprint import comments_bp 
from blueprints.communities import communities_bp
from blueprints.experts_blue import expert_blueprint 
from blueprints.likes_blue import likes_bp
from blueprints.messages_blueprint import message_blueprint

load_dotenv()

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agriconnect.db'


# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
CORS(app)


app.register_blueprint(auth_blueprint)
app.register_blueprint(blogs_bp)
app.register_blueprint(comments_bp)
app.register_blueprint(communities_bp)
app.register_blueprint(expert_blueprint)
app.register_blueprint(likes_bp)
app.register_blueprint(message_blueprint)



if __name__ == "__main__":
    app.run(port=8081, debug=True)
