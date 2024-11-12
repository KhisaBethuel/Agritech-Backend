from flask import Flask, make_response, request, jsonify, Blueprint
from flask_migrate import Migrate
from models import *
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required
from flask_cors import CORS
from dotenv import load_dotenv
import os

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

# Define Blueprint
api = Blueprint('api', __name__)

# 1. Signup Route
@api.route('/signup', methods=['POST'])
def signup():
    try:
        # Create a new user
        new_user = Signup(
            username=request.json.get("username"),
            password=request.json.get("password")
        )

        db.session.add(new_user)
        db.session.commit()

        # Generate JWT tokens
        access_token = create_access_token(identity=new_user.id)
        refresh_token = create_refresh_token(identity=new_user.id)

        response_body = {
            "user": new_user.to_dict(),
            "access_token": access_token,
            "refresh_token": refresh_token
        }
        return make_response(response_body, 201)

    except Exception as e:
        print(e)  # Logging for debugging
        return make_response({"errors": ["Signup failed"]}, 400)

# 2. Login Route
@api.route('/login', methods=['POST'])
def login():
    try:
        # Authenticate user
        user = Login.query.filter_by(username=request.json.get("username")).first()
        if user and user.check_password(request.json.get("password")):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)

            response_body = {
                "user": user.to_dict(),
                "access_token": access_token,
                "refresh_token": refresh_token
            }
            return make_response(response_body, 200)

        return make_response({"errors": ["Invalid credentials"]}, 401)

    except Exception as e:
        print(e)  # Logging for debugging
        return make_response({"errors": ["Login failed"]}, 400)

# 3. CRUD Operations for Blogs
@api.route('/blogs', methods=['GET', 'POST'])
def blogs():
    if request.method == 'POST':
        try:
            new_blog = Blog(
                title=request.json.get("title"),
                content=request.json.get("content")  # Assume content field exists
            )
            db.session.add(new_blog)
            db.session.commit()

            response_body = new_blog.to_dict()
            return make_response(response_body, 201)
        except Exception as e:
            print(e)  # Logging for debugging
            return make_response({"errors": ["Failed to create blog"]}, 400)

    elif request.method == 'GET':
        blogs = [blog.to_dict() for blog in Blog.query.all()]
        return make_response(jsonify(blogs), 200)

@api.route('/blogs/<int:blog_id>', methods=['GET', 'PUT', 'DELETE'])
def blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog is None:
        return make_response({"error": "Blog not found"}, 404)

    if request.method == 'GET':
        return make_response(blog.to_dict(), 200)

    elif request.method == 'PUT':
        try:
            data = request.get_json()
            blog.title = data.get("title", blog.title)
            blog.content = data.get("content", blog.content)
            db.session.commit()
            return make_response(blog.to_dict(), 200)
        except Exception as e:
            print(e)  
            return make_response({"errors": ["Failed to update blog"]}, 400)

    elif request.method == 'DELETE':
        try:
            db.session.delete(blog)
            db.session.commit()
            return make_response({"message": "Blog deleted successfully"}, 204)
        except Exception as e:
            print(e)  
            return make_response({"errors": ["Failed to delete blog"]}, 400)

# Register Blueprint
app.register_blueprint(api, url_prefix='/api')

# CRUD Operations for Experts
@api.route('/experts', methods=['GET', 'POST'])
def experts():
    if request.method == 'POST':
        try:
            new_expert = Expert(
                name=request.json.get("name"),
                field=request.json.get("field")
            )
            db.session.add(new_expert)
            db.session.commit()
            return make_response(new_expert.to_dict(), 201)
        except Exception as e:
            return make_response({"errors": ["Failed to create expert"]}, 400)

    elif request.method == 'GET':
        experts = [expert.to_dict() for expert in Expert.query.all()]
        return make_response(jsonify(experts), 200)

@api.route('/experts/<int:expert_id>', methods=['GET', 'PUT', 'DELETE'])
def expert(expert_id):
    expert = Expert.query.get(expert_id)
    if not expert:
        return make_response({"error": "Expert not found"}, 404)

    if request.method == 'GET':
        return make_response(expert.to_dict(), 200)
    
    elif request.method == 'PUT':
        data = request.get_json()
        expert.name = data.get("name", expert.name)
        expert.field = data.get("field", expert.field)
        db.session.commit()
        return make_response(expert.to_dict(), 200)

    elif request.method == 'DELETE':
        db.session.delete(expert)
        db.session.commit()
        return make_response({"message": "Expert deleted successfully"}, 204)


# CRUD Operations for Messages
@api.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        try:
            new_message = Message(
                content=request.json.get("content"),
                sender_id=request.json.get("sender_id"),
                recipient_id=request.json.get("recipient_id")
            )
            db.session.add(new_message)
            db.session.commit()
            return make_response(new_message.to_dict(), 201)
        except Exception as e:
            return make_response({"errors": ["Failed to create message"]}, 400)

    elif request.method == 'GET':
        messages = [message.to_dict() for message in Message.query.all()]
        return make_response(jsonify(messages), 200)

@api.route('/messages/<int:message_id>', methods=['GET', 'PUT', 'DELETE'])
def message(message_id):
    message = Message.query.get(message_id)
    if not message:
        return make_response({"error": "Message not found"}, 404)

    if request.method == 'GET':
        return make_response(message.to_dict(), 200)

    elif request.method == 'PUT':
        data = request.get_json()
        message.content = data.get("content", message.content)
        db.session.commit()
        return make_response(message.to_dict(), 200)

    elif request.method == 'DELETE':
        db.session.delete(message)
        db.session.commit()
        return make_response({"message": "Message deleted successfully"}, 204)


# CRUD Operations for Likes
@api.route('/likes', methods=['POST'])
def create_like():
    try:
        new_like = Like(
            user_id=request.json.get("user_id"),
            post_id=request.json.get("post_id")
        )
        db.session.add(new_like)
        db.session.commit()
        return make_response(new_like.to_dict(), 201)
    except Exception as e:
        return make_response({"errors": ["Failed to create like"]}, 400)

@api.route('/likes/<int:like_id>', methods=['DELETE'])
def delete_like(like_id):
    like = Like.query.get(like_id)
    if not like:
        return make_response({"error": "Like not found"}, 404)

    db.session.delete(like)
    db.session.commit()
    return make_response({"message": "Like deleted successfully"}, 204)


# CRUD Operations for Comments
@api.route('/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'POST':
        try:
            new_comment = Comment(
                content=request.json.get("content"),
                user_id=request.json.get("user_id"),
                post_id=request.json.get("post_id")
            )
            db.session.add(new_comment)
            db.session.commit()
            return make_response(new_comment.to_dict(), 201)
        except Exception as e:
            return make_response({"errors": ["Failed to create comment"]}, 400)

    elif request.method == 'GET':
        comments = [comment.to_dict() for comment in Comment.query.all()]
        return make_response(jsonify(comments), 200)

@api.route('/comments/<int:comment_id>', methods=['GET', 'PUT', 'DELETE'])
def comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        return make_response({"error": "Comment not found"}, 404)

    if request.method == 'GET':
        return make_response(comment.to_dict(), 200)

    elif request.method == 'PUT':
        data = request.get_json()
        comment.content = data.get("content", comment.content)
        db.session.commit()
        return make_response(comment.to_dict(), 200)

    elif request.method == 'DELETE':
        db.session.delete(comment)
        db.session.commit()
        return make_response({"message": "Comment deleted successfully"}, 204)


# CRUD Operations for Communities
@api.route('/communities', methods=['GET', 'POST'])
def communities():
    if request.method == 'POST':
        try:
            new_community = Community(
                name=request.json.get("name"),
                description=request.json.get("description")
            )
            db.session.add(new_community)
            db.session.commit()
            return make_response(new_community.to_dict(), 201)
        except Exception as e:
            return make_response({"errors": ["Failed to create community"]}, 400)

    elif request.method == 'GET':
        communities = [community.to_dict() for community in Community.query.all()]
        return make_response(jsonify(communities), 200)

@api.route('/communities/<int:community_id>', methods=['GET', 'PUT', 'DELETE'])
def community(community_id):
    community = Community.query.get(community_id)
    if not community:
        return make_response({"error": "Community not found"}, 404)

    if request.method == 'GET':
        return make_response(community.to_dict(), 200)

    elif request.method == 'PUT':
        data = request.get_json()
        community.name = data.get("name", community.name)
        community.description = data.get("description", community.description)
        db.session.commit()
        return make_response(community.to_dict(), 200)

    elif request.method == 'DELETE':
        db.session.delete(community)
        db.session.commit()
        return make_response({"message": "Community deleted successfully"}, 204)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
